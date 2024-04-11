# pylint: disable-next=no-name-in-module
from PyQt6.QtWidgets import QMainWindow, QVBoxLayout
from transactions_model import TransactionsModel
from table_widget import TableWidget
from table_widget_controller import TableWidgetController

class View(QMainWindow,):
    def __init__(self, model: TransactionsModel):
        super().__init__()
        self.setWindowTitle("CATEGORISE")
        layout = QVBoxLayout()
        self.table = TableWidget(model)
        self.controller = None

        layout.addWidget(self.table)
        self.setCentralWidget(self.table)
    
    def show(self):
        self.show()

    def set_controller(self, controller: TableWidgetController):
        self.controller = controller

