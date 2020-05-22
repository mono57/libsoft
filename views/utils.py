from PyQt5.QtWidgets import QMessageBox

def get_index_table(widget, table_view):
    indexes = table_view.selectedIndexes()

    if not indexes:
        QMessageBox.information(
            widget, 'Info', 'Veuillez faire une selection', QMessageBox.Yes)
        return None, None

    if len(indexes) >= 2:
        QMessageBox.information(
            widget, 'Info', 'Les actions groupées ne sont pas permises !', QMessageBox.Yes)
        return None, None

    row = table_view.currentIndex().row()
    index = table_view.model().index(row, 0)

    return row, index


def get_data_by_model_pk(object_list, pk):
    return [ obj for obj in object_list if obj.id == pk ][0]