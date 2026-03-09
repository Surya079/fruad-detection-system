# Later we can reuse this model for:

# Kafka messages

# Spark schema

# ML dataset

class Transaction:
    def __init__(self,transaction_id,customer_id,
                 amount,currency, merchant_id,merchant_category, 
                 transaction_type,transaction_time,
                 country,device_id):
        
        self.transaction_id = transaction_id
        self.customer_id= customer_id
        self.amount=amount
        self.currency= currency
        self.merchant_id=merchant_id
        self.merchant_category=merchant_category
        self.transaction_type= transaction_type
        self.transaction_time= transaction_time
        self.country= country
        self.device_id= device_id


