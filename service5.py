import time
from sql_queries import create_table, insert_transaction
from transaction import Transaction
import random

create_table()

# симуляция инфляции цен
# они теперь будут расти на 1-100 рублей каждые 10 секунд

if __name__ == '__main__':
    while True:
        insert_transaction(
            Transaction(
              price = random.randint(1, 100),
              quantity = random.randint(1, 100),
              description="service5",
              amount=0,
            )
        )
        print("service5: new transaction")
        time.sleep(10)
