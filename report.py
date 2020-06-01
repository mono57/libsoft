from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib.units import cm, inch

doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
# container for the 'Flowable' objects

styles = getSampleStyleSheet()
styleNormal = styles['Normal']

elements = []

header = ['Quantité', 'Article', 'Prix en F CFA', 'Client', 'Date', 'Montant']

data = [
    header,
    [1, 'Le bible du seigneur', '1000 ', 'Amono', '2020.20.20', '1000 '],
    [1, 'elit erat euismod orci, ac placerat dolor lectus quis orci.',
        '1000 ', 'Amono', '2020.20.20', '1000 '],
    [1, 'Le bible du seigneur', '1000 ', 'Amono', '2020.20.20', '1000 '],
    [1, 'Le bible du seigneur', '1000 ', 'Amono', '2020.20.20', '1000 '],
]

line1 = 'CENTRE BIBLIQUE NGAOUNDERE'
line2 = 'Date du: {}'.format(datetime.datetime.now().strftime("%d-%m-%y"))
line4 = 'RAPPORT DE VENTES'
line5 = 'Période allant de : {} à {}'.format(datetime.datetime.now().strftime(
    "%d-%m-%y"), datetime.datetime.now().strftime("%d-%m-%y"))

elements.append(Paragraph(line1, styleNormal))
elements.append(Paragraph(line2, styleNormal))
elements.append(Spacer(inch, .25 * inch))
elements.append(Paragraph(line4, styleNormal))
elements.append(Paragraph(line5, styleNormal))
elements.append(Spacer(inch, .25 * inch))


t = Table(data)
t.setStyle(TableStyle([
    ('ALIGN', (2, 2), (-1, -1), 'CENTER'),
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

doc.build(elements)
