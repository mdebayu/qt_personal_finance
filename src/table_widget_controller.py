""" Controller """
from transactions_model import TransactionsModel
from table_widget import TableWidget
class TableWidgetController:
    """ Controller """
    def __init__(self, model: TransactionsModel, view: TableWidget):
        self.model = model
        self.view = view
