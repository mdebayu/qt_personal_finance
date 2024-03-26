"""Table Widget"""
from operator import attrgetter
from functools import partial

# pylint: disable=no-name-in-module
from PyQt6.QtGui import QMouseEvent, QWheelEvent
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWidgets import QHBoxLayout,QLabel, QComboBox, QPushButton,QFileDialog
# pylint: enable=no-name-in-module

from transaction import Transaction


# TODO: Add row highlighting on clicking on a row
# TODO: Add shift click after click to select multiple rows
# TODO: Add right click for menu and select "Duplicate Categories"
# TODO: Add shortcut of CTRL+C and CTRL+V


def clamp(val: int|float, _min: int|float, _max: int|float):
    """Clamp val between _min and _max"""
    return max(_min, min(val,_max))

def get_cat_combobox(txn: Transaction, categories):
    """Provides a ComboBox"""
    combobox = QComboBox()
    combobox.addItems(categories)
    if txn.category in categories:
        combobox.setCurrentIndex(categories.index(txn.category))

    def on_change():
        txn.category = combobox.currentText()

    combobox.currentIndexChanged.connect(on_change)
    return combobox

class ClickLabel(QLabel):
    """Clickable Label"""
    def __init__(self,layout: QHBoxLayout, name: str, fn):
        super().__init__()
        self.setText(name)
        self.fn = fn
        layout.addWidget(self)

    # pylint: disable-next=invalid-name
    def mousePressEvent(self, ev: QMouseEvent | None) -> None:
        """Override Mousepress"""
        self.fn()

        return super().mousePressEvent(ev)


class HeaderWidget(QWidget):
    """Header Row"""
    def __init__(self,fn):
        super().__init__()
        self.setObjectName("HeaderWidget")
        self.setAutoFillBackground(True)

        layout = QHBoxLayout()
        self.indx_btn = ClickLabel(layout,"Index",partial(fn,"index"))
        self.account_btn = ClickLabel(layout, "Account",partial(fn,"account"))
        self.date_btn = ClickLabel(layout,"Date",partial(fn,"date"))
        self.desc_btn = ClickLabel(layout,"Description",partial(fn,"desc"))
        self.desc_btn.setObjectName("Desc")
        self.amount_btn = ClickLabel(layout,str("Amount"),partial(fn,"amount"))
        self.cat_btn = ClickLabel(layout, "Category", partial(fn,"category"))


        self.setLayout(layout)

class RowWidget(QWidget):
    """Representation of a Row"""
    def __init__(self,tx: Transaction,categories: list[str]):
        super().__init__()
        self.selected = False
        layout = QHBoxLayout()
        layout.addWidget(QLabel(str(tx.index)))
        layout.addWidget(QLabel(tx.account))
        layout.addWidget(QLabel(tx.date))
        desc = QLabel(tx.desc)
        desc.setObjectName("Desc")
        layout.addWidget(desc)
        layout.addWidget(QLabel(str(tx.amount)))
        layout.addWidget(get_cat_combobox(tx,categories))

        self.setLayout(layout)

class TopButtonsWidget(QWidget):
    """Buttons at the Top"""
    def __init__(self, export_fn, import_fn):
        super().__init__()
        self.setObjectName("TopButtonsWidget")
        layout = QHBoxLayout()

        import_btn = QPushButton("Import")
        import_btn.clicked.connect(import_fn)

        export_btn = QPushButton("Export")
        export_btn.clicked.connect(export_fn)

        layout.addWidget(import_btn)
        layout.addWidget(export_btn)
        self.setLayout(layout)


class TableWidget(QWidget):
    """Table Widget"""
    def __init__(self, tx_list: list[Transaction], cfg=dict):
        super().__init__()
        self.setObjectName("TableWidget")
        self.sort_col :dict[str,bool] = {}

        self._index = cfg["start_index"] #pyright: ignore[reportUndefinedVariable]
        self._num = cfg["show_count"] #pyright: ignore[reportUndefinedVariable]
        self.categories = cfg["categories"] #pyright: ignore[reportUndefinedVariable]

        self.tx_list = tx_list
        self.max_index = len(tx_list)

        self._layout = QVBoxLayout()
        self._layout.addWidget(TopButtonsWidget(self._export, self._import))
        self._layout.insertStretch(1,1)
        self._layout.addWidget(HeaderWidget(self._sort_by_col))

        self._refresh_rows()
        self.setLayout(self._layout)

    def _import(self):
        fin = QFileDialog.getExistingDirectory(self, caption="Import Directory")
        print(f"import files from {fin}")

    def _export(self):
        fout = QFileDialog.getSaveFileName(self,caption="Export Filename",
                                            filter=self.tr("Comma Separated Values (*.csv)"))

        if fout[0].strip() ==  "":
            return

        fname = fout[0]
        with open(fname,"w",encoding="utf-8") as fw:
            for txn in self.tx_list:
                fw.write(txn.csv_str + "\n")


    def _sort_by_col(self, col_name: str):
        if col_name in self.sort_col:
            self.sort_col[col_name] = not self.sort_col[col_name]
        else:
            self.sort_col[col_name] = False
        rev = self.sort_col[col_name]
        self.tx_list = sorted(self.tx_list,key=attrgetter(col_name),reverse=rev)
        self._refresh_rows()

    def _refresh_rows(self):
        for w in self.children():
            if isinstance(w,RowWidget):
                w.deleteLater()
        for i in range(self._index,min(self._index+self._num,len(self.tx_list))):
            self._layout.addWidget(RowWidget(self.tx_list[i],self.categories))

    #pylint: disable-next=invalid-name
    def wheelEvent(self, a0: QWheelEvent | None) -> None:
        """Override the Wheel Event to capture Mouse Wheels"""
        if a0 is None:
            return super().wheelEvent(a0)

        counts =  int(a0.angleDelta().y()/-120.0)
        self._index = clamp(self._index + counts, 0,self.max_index-self._num)

        self._refresh_rows()

        return super().wheelEvent(a0)
