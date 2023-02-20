import time
import random
from sql_queries import create_table, insert_transaction
from transaction import Transaction

create_table()

if __name__ == '__main__':
    while True:
        insert_transaction(
            Transaction(
                description=random.choice(["halyk", "kaspi", "forte", "kazkommertsbank", "kazpostbank"]),
                price=random.randint(-100, 100),
                quantity=random.randint(0, 10),
                amount=0,
                sender="krivalex",
                receiver="timur",
                sender_id=666,
                receiver_id=228,
            )
        )
        print("Add new Bank transaction")
        time.sleep(10)
