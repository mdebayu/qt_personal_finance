from transaction import Transaction
from pathlib import Path
from functools import partial
import re

ACC_NAME_REGEX = re.compile(r"\d{2}_\d{2}_\d{2}_(?P<acc_name>\w+_\w+)")

def ing_line_to_txn(line: str, account: str)->Transaction:
    # 28/03/2024,"ANUSHKA GOSWAMI For the tyre - Osko Payment - Receipt 52734 ",199.00,,7063.83
    date_str,desc,credit,debit,balance = line.split(",")
    return Transaction(account,date_str,desc,credit,debit,balance,None)
     
def account_name_from_filename(fname: str)->str:
    res = ACC_NAME_REGEX.match(fname)
    if res is not None:
        return res.group("acc_name")
    else:
        return fname

def read_file(fpath: str)->list[Transaction]:
    txns : list[Transaction] = list()
    path = Path(fpath)
    account_name = account_name_from_filename(path.name)
    parse_fn = partial(ing_line_to_txn,account=account_name)
    with open(path,'r') as fr:
        fr.readline()
        for line in fr.readlines():
            txns.append(parse_fn(line))
    return txns

if __name__ == "__main__":
    txns = read_file("data/2025_transactions/24_03_29_AG_EVSP.csv")
    print(txns)