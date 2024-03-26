"""Creates a Table widget"""
import sys
# pylint: disable-next=no-name-in-module
from PyQt6.QtWidgets import QApplication,QMainWindow, QVBoxLayout

from transaction import Transaction
from config import get_cfg
from table_widget import TableWidget

def main_gui():
    """Start the GUI"""
    app = QApplication(sys.argv)
    cfg = get_cfg("data/settings.toml")

    transactions = [
        Transaction("acc1","23Nov12","desc1",123.12,"n/a"),
        Transaction("acc1","23Nov12","desdnlakjdsnbfkasc1",538.12,"n/a"),
        Transaction("acc1","23Nov12","descad;slmflakdsfm1",1689.12,"n/a"),
        Transaction("acc1","23Nov12","desca;sdknf;as1",1789.12,"n/a"),
        Transaction("acc1","23Nov12","dajksdbnfaesc1",179.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",174.12,"n/a"),
        Transaction("acc1","23Nov12","descasdfasd1",6243.12,"n/a"),
        Transaction("acc1","23Nov12","descakjdb1",6343.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",6373.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",333.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",123.12,"n/a"),
        Transaction("acc1","23Nov12","desdnlakjdsnbfkasc1",538.12,"n/a"),
        Transaction("acc1","23Nov12","descad;slmflakdsfm1",1689.12,"n/a"),
        Transaction("acc1","23Nov12","desca;sdknf;as1",1789.12,"n/a"),
        Transaction("acc1","23Nov12","dajksdbnfaesc1",179.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",174.12,"n/a"),
        Transaction("acc1","23Nov12","descasdfasd1",6243.12,"n/a"),
        Transaction("acc1","23Nov12","descakjdb1",6343.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",6373.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",333.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",123.12,"n/a"),
        Transaction("acc1","23Nov12","desdnlakjdsnbfkasc1",538.12,"n/a"),
        Transaction("acc1","23Nov12","descad;slmflakdsfm1",1689.12,"n/a"),
        Transaction("acc1","23Nov12","desca;sdknf;as1",1789.12,"n/a"),
        Transaction("acc1","23Nov12","dajksdbnfaesc1",179.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",174.12,"n/a"),
        Transaction("acc1","23Nov12","descasdfasd1",6243.12,"n/a"),
        Transaction("acc1","23Nov12","descakjdb1",6343.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",6373.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",333.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",123.12,"n/a"),
        Transaction("acc1","23Nov12","desdnlakjdsnbfkasc1",538.12,"n/a"),
        Transaction("acc1","23Nov12","descad;slmflakdsfm1",1689.12,"n/a"),
        Transaction("acc1","23Nov12","desca;sdknf;as1",1789.12,"n/a"),
        Transaction("acc1","23Nov12","dajksdbnfaesc1",179.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",174.12,"n/a"),
        Transaction("acc1","23Nov12","descasdfasd1",6243.12,"n/a"),
        Transaction("acc1","23Nov12","descakjdb1",6343.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",6373.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",333.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",123.12,"n/a"),
        Transaction("acc1","23Nov12","desdnlakjdsnbfkasc1",538.12,"n/a"),
        Transaction("acc1","23Nov12","descad;slmflakdsfm1",1689.12,"n/a"),
        Transaction("acc1","23Nov12","desca;sdknf;as1",1789.12,"n/a"),
        Transaction("acc1","23Nov12","dajksdbnfaesc1",179.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",174.12,"n/a"),
        Transaction("acc1","23Nov12","descasdfasd1",6243.12,"n/a"),
        Transaction("acc1","23Nov12","descakjdb1",6343.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",6373.12,"n/a"),
        Transaction("acc1","23Nov12","desc1",333.12,"n/a"),
    ]


    window = QMainWindow()
    window.setWindowTitle("CATEGORIZE")
    layout = QVBoxLayout()
    table = TableWidget(transactions,cfg["table_settings"])
    layout.addWidget(table)
    window.setCentralWidget(table)

    window.show()
    app.setStyleSheet(open(cfg["stylesheet"],encoding="utf-8").read())
    app.exec()
if __name__ == "__main__":
    main_gui()
