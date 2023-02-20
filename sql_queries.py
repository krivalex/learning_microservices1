import psycopg2

from transaction import Transaction

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS transactions_krivalex2 (
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        sender VARCHAR(255) NOT NULL,
        receiver VARCHAR(255) NOT NULL,
        sender_id INTEGER NOT NULL,
        receiver_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        amount INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'new'
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_transaction(transaction: Transaction):
    query = """
    INSERT INTO transactions_krivalex2 (description, price, sender, receiver, sender_id, receiver_id, quantity, amount)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (transaction.description, transaction.price, transaction.sender, transaction.receiver, transaction.sender_id, 
                           transaction.receiver_id, transaction.quantity, transaction.amount))
    conn.commit()


def update_transactions():
    query = "UPDATE transactions_krivalex2 SET amount=price*quantity, status='calculated' WHERE status='new';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def complete_transactions():
    query = "UPDATE transactions_krivalex2 SET status='completed' WHERE status='calculated';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def get_transactions() -> list[Transaction]:
    query = "SELECT * FROM transactions_krivalex2;"
    cursor = conn.cursor()
    cursor.execute(query)
    return [Transaction(
        id=transaction[0],
        description=transaction[1],
        price=transaction[2],
        sender=transaction[3],
        receiver=transaction[4],
        sender_id=transaction[5],
        receiver_id=transaction[6],
        quantity=transaction[7],
        amount=transaction[8],
        created=transaction[9],
        status=transaction[10],

    ) for transaction in cursor.fetchall()]

