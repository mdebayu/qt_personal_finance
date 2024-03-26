"""Transaction Dataclass"""
from dataclasses import dataclass, field
from itertools import count

@dataclass
class Transaction:
    """Transaction"""
    account: str
    date: str
    desc: str
    amount: float
    category: str
    index: int = field(default_factory=count().__next__)

    @property
    def csv_str(self) -> str:
        """Returns a Comma Separated Value Str"""
        t=self
        return f"{t.index},{t.account},{t.date},{t.desc},{t.amount:0.2f},{t.category}"
