# Efficient DB writer for batch inserts

import oracledb
from config import DB_USER, DB_PASSWORD, DB_DSN

BATCH_SIZE = 100

connection = None
cursor = None


def init_connection():
    global connection, cursor

    connection = oracledb.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        dsn=DB_DSN
    )

    cursor = connection.cursor()

    print("Oracle connection initialized")


def insert_batch(transactions):

    query = """
    MERGE INTO RAW_TRANSACTIONS t
    USING (SELECT :transaction_id AS transaction_id FROM dual) s
    ON (t.TRANSACTION_ID = s.transaction_id)
    WHEN NOT MATCHED THEN
    INSERT (
        TRANSACTION_ID,
        CUSTOMER_ID,
        AMOUNT,
        CURRENCY,
        MERCHANT_ID,
        MERCHANT_CATEGORY,
        TRANSACTION_TYPE,
        TRANSACTION_TIME,
        COUNTRY,
        DEVICE_ID
    )
    VALUES (
        :transaction_id,
        :customer_id,
        :amount,
        :currency,
        :merchant_id,
        :merchant_category,
        :transaction_type,
        :transaction_time,
        :country,
        :device_id
    )
    """

    cursor.executemany(query, transactions)

    connection.commit()

    print(f"Committed batch of {len(transactions)} transactions")