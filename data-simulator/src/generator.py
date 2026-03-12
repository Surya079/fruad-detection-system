import uuid
import random
import time
from faker import Faker
from datetime import datetime
from db_writter import init_connection, insert_batch 

fake = Faker()

BATCH_SIZE = 100


def generate_transaction():

    return {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": f"CUST{random.randint(1000,9999)}",
        "amount": round(random.uniform(10, 2000), 2),
        "currency": "USD",
        "merchant_id": f"MERCH{random.randint(100,999)}",
        "merchant_category": random.choice(["GROCERY", "TRAVEL", "ELECTRONICS"]),
        "transaction_type": random.choice(["ONLINE", "POS"]),
        "transaction_time": datetime.now(),
        "country": random.choice(["US", "UK", "IN"]),
        "device_id": f"DEV{random.randint(10000,99999)}"
    }


def run_generator():

    init_connection()

    batch = []

    while True:

        txn = generate_transaction()

        batch.append(txn)

        if len(batch) >= BATCH_SIZE:

            insert_batch(batch)

            batch.clear()

        time.sleep(60)


if __name__ == "__main__":
    run_generator()