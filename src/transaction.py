"""Transaction Dataclass"""
from dataclasses import dataclass, field
from itertools import count
from datetime import datetime

@dataclass
class Transaction:
    """Transaction"""
    account: str
    date_obj: datetime
    desc: str
    credit: float
    debit: float
    category: str
    index: int = field(default_factory=count().__next__)

    @property
    def date(self):
        return self.date_obj.strftime(r"%d-%b-%y")

    @property
    def csv_str(self) -> str:
        """Returns a Comma Separated Value Str"""
        t=self
        return f"{t.index},{t.account},{t.date},{t.desc},{t.amount:0.2f},{t.category}"
