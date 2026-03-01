import uuid
import random
import time
from datetime import datetime, timezone
import requests

# Use port 8082 (HTTP) - this goes to your processor
NIFI_ENDPOINTS = "http://localhost:8081/transactions"

def generate_transactions():    
    return {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": f"C{random.randint(1000, 9999)}",
        "amount": round(random.uniform(10, 50000),2 ),
        "currency": "INR",
        "merchant_id": f"M{random.randint(100, 999)}",
        "merchant_category": random.choice(["ECOMMERCE", "ATM", "POS"]),
        "transaction_type": random.choice(["ONLINE", "ATM", "POS"]),
        "transaction_time": datetime.now(timezone.utc).isoformat(),
        "country": "IN",
        "device_id": f"device-{random.randint(1, 50)}"
    }

while True:
    txn = generate_transactions()
    try:
        response = requests.post(
            NIFI_ENDPOINTS, 
            json=txn, 
            timeout=5,
            headers={'Content-Type': 'application/json'}
        )
        print(f"✅ Sent: {txn['transaction_id']} - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")
    time.sleep(1)