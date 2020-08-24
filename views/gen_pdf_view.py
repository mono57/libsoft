from PyQt5.QtWidgets import QDialog

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib.units import cm, inch
import time
from views.layout.GenPDFWindow import Ui_GenPdfWidget

import sys


class GenPDFView(QDialog, Ui_GenPdfWidget):
    def __init__(self, collection, periods=None, is_inventaire=False, header=None, parent=None):
        super(GenPDFView, self).__init__(parent)
        self.setupUi(self)

        self.collection = collection
        self.periods = periods
        self.header = header or ['Article', 'Quantité',
                                 'Prix ( F CFA)', 'Montant (F CFA)', 'Client', 'Date de vente', ]

        if is_inventaire:
            self.process_gen_inventaire()
        else:
            if header:
                self.process_gen_rapport_command()
            else:
                self.process_gen_pdf()

        self.close()

    def process_gen_inventaire(self):
        styles = getSampleStyleSheet()
        styleNormal = styles['Normal']

        elements = []

        data = [
            ['No', 'Designation', 'Qté vendu', 'Qté en stock'],

        ]

        for index, article in enumerate(self.collection):
            row = []
            row.append(Paragraph(str(index+1), styleNormal))
            row.append(Paragraph(article.designation, styleNormal))
            row.append(Paragraph(str(len(article.selling_entry)), styleNormal))
            row.append(Paragraph(str(article.quantity), styleNormal))

            data.append(row)
            value = (100/len(self.collection))*(index + 1)

            self.progressBar.setValue(value)

        today = datetime.datetime.now()
        line1 = 'CENTRE BIBLIQUE NGAOUNDERE'
        line2 = 'Date du: {}'.format(
            today.strftime("%d %b %Y"))
        line4 = 'Inventaire d\'article(s)'
        # line5 = 'Période allant du : {} au {}'.format(self.periods.get('start').strftime(
        #     "%d %b %Y"), self.periods.get('end').strftime("%d %b %Y"))

        elements.append(Paragraph(line1, styleNormal))
        elements.append(Paragraph(line2, styleNormal))
        elements.append(Spacer(inch, .25 * inch))
        elements.append(Paragraph(line4, styleNormal))

        elements.append(Spacer(inch, .25 * inch))

        t = Table(data)
        t.setStyle(TableStyle([
            # ('ALIGN', (2, 2), (-1, -1), 'CENTER'),
            #    ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
            #    ('VALIGN', (0, 0), (0, -1), 'TOP'),
            #    ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
            #    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
            #    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
            #    ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
        elements.append(t)
        elements.append(Spacer(inch, .25*inch))
        # elements.append(Paragraph(
        #     'Montant Total des ventes : {} F CFA'.format(total_cost), styleNormal))

        filename = 'rapport_inventaire_{}.pdf'.format(
            today.strftime("%d %b %Y"))

        doc = SimpleDocTemplate(filename, pagesize=letter)

        doc.build(elements)

    def process_gen_rapport_command(self):
        styles = getSampleStyleSheet()
        styleNormal = styles['Normal']

        elements = []

        data = [
            self.header,

        ]

        total_command = []
        for index, command in enumerate(self.collection):
            prices = []
            for entry in command.command_entries:
                row = []
                qte, article = entry.cmd_qte, entry.article
                row.append(Paragraph(article.designation, styleNormal))
                row.append(Paragraph(str(qte), styleNormal))
                # row.append(Paragraph(str(price), styleNormal))
                row.append(Paragraph(command.provider.full_name, styleNormal))
                row.append(
                    Paragraph(command.date_reception.strftime("%d-%m-%Y"), styleNormal))

                data.append(row)

            # selling_discount = command.selling_discount
            # discount = int(selling_discount) if selling_discount else 0
            # total_price = sum(prices)
            # total_command.append(total_price - total_price * discount//100)
            value = (100/len(self.collection))*(index + 1)

            self.progressBar.setValue(value)

        total_cost = sum(total_command)

        line1 = 'CENTRE BIBLIQUE NGAOUNDERE'
        line2 = 'Date du: {}'.format(
            datetime.datetime.now().strftime("%d %b %Y"))
        line4 = 'RAPPORT DE COMMANDES'
        

        elements.append(Paragraph(line1, styleNormal))
        elements.append(Paragraph(line2, styleNormal))
        elements.append(Spacer(inch, .25 * inch))
        elements.append(Paragraph(line4, styleNormal))

        if self.periods:
            line5 = 'Période allant du : {} au {}'.format(self.periods.get('start').strftime(
                "%d %b %Y"), self.periods.get('end').strftime("%d %b %Y"))
            elements.append(Paragraph(line5, styleNormal))
            
        elements.append(Spacer(inch, .25 * inch))

        t = Table(data)
        t.setStyle(TableStyle([
            # ('ALIGN', (2, 2), (-1, -1), 'CENTER'),
            #    ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
            #    ('VALIGN', (0, 0), (0, -1), 'TOP'),
            #    ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
            #    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
            #    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
            #    ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
        elements.append(t)
        elements.append(Spacer(inch, .25*inch))
        # elements.append(Paragraph(
        #     'Montant Total des ventes : {} F CFA'.format(total_cost), styleNormal))

        filename = 'rapport_command_{}_{}.pdf'.format(
            self.periods.get('start'), self.periods.get('end'))

        doc = SimpleDocTemplate(filename, pagesize=letter)

        doc.build(elements)

    def process_gen_pdf(self):

        # container for the 'Flowable' objects
        styles = getSampleStyleSheet()
        styleNormal = styles['Normal']

        elements = []

        data = [
            self.header,

        ]

        total_selling = []
        for index, selling in enumerate(self.collection):
            prices = []
            for entry in selling.selling_entries:
                row = []
                qte, article = entry.selling_qte, entry.article
                row.append(Paragraph(article.designation, styleNormal))
                row.append(Paragraph(str(qte), styleNormal))
                selling_price = article.selling_price
                row.append(Paragraph(selling_price, styleNormal))
                price = qte * int(float(selling_price))
                prices.append(price)
                row.append(Paragraph(str(price), styleNormal))
                row.append(Paragraph(selling.client, styleNormal))
                row.append(
                    Paragraph(selling.selling_date.strftime("%d-%m-%Y"), styleNormal))

                data.append(row)

            selling_discount = selling.selling_discount
            discount = int(selling_discount) if selling_discount else 0
            total_price = sum(prices)
            total_selling.append(total_price - total_price * discount//100)
            value = (100/len(self.collection))*(index + 1)

            # self.progressBar.setValue(value)

        total_cost = sum(total_selling)

        line1 = 'CENTRE BIBLIQUE NGAOUNDERE'
        line2 = 'Date du: {}'.format(
            datetime.datetime.now().strftime("%d %b %Y"))
        line4 = 'RAPPORT DE VENTES'
        line5 = 'Période allant du : {} au {}'.format(self.periods.get('start').strftime(
            "%d %b %Y"), self.periods.get('end').strftime("%d %b %Y"))

        elements.append(Paragraph(line1, styleNormal))
        elements.append(Paragraph(line2, styleNormal))
        elements.append(Spacer(inch, .25 * inch))
        elements.append(Paragraph(line4, styleNormal))
        elements.append(Paragraph(line5, styleNormal))
        elements.append(Spacer(inch, .25 * inch))

        t = Table(data)
        t.setStyle(TableStyle([
            # ('ALIGN', (2, 2), (-1, -1), 'CENTER'),
            #    ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
            #    ('VALIGN', (0, 0), (0, -1), 'TOP'),
            #    ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
            #    ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
            #    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
            #    ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
        elements.append(t)
        elements.append(Spacer(inch, .25*inch))
        elements.append(Paragraph(
            'Montant Total des ventes : {} F CFA'.format(total_cost), styleNormal))

        filename = 'rapport_vente_{}_{}.pdf'.format(
            self.periods.get('start'), self.periods.get('end'))

        doc = SimpleDocTemplate(filename, pagesize=letter)

        doc.build(elements)
