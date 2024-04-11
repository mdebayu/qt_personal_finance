"""" Model """
from transaction import Transaction

class TransactionsModel:
    """" Model of Transactions """
    def __init__(self, transaction_list: list[Transaction]):
        self._txns = transaction_list
    @property
    def txns(self) -> list[Transaction]:
        """Get Transactions"""
        return self._txns
