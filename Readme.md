# project repository structure

```

    fraud-detection-platform/
    │
    ├── docker-compose/
    │
    │
    ├── database/
    │
    │
    ├── data-simulator/
    │
    ├── ingestion/
    │
    │
    ├── streaming/
    │
    │
    ├── services/
    │
    ├── ml-model/
    │
    │
    ├── frontend/
    │
    ├── hadoop/
    │
    │
    ├── infrastructure/
    │
    │
    └── scripts/

```

## Raw Transaction Schema

```
    {
        "transaction_id": "uuid",
        "customer_id": "string",
        "amount": 1250.50,
        "currency": "INR",
        "merchant_id": "M123",
        "merchant_category": "ECOMMERCE",
        "transaction_type": "ONLINE",
        "transaction_time": "2026-02-27T10:30:00Z",
        "country": "IN",
        "device_id": "device-abc-123"
    }

```

# Spark submit command

```
   /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --conf spark.jars.ivy=/opt/spark/ivy-cache \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.1 \
  /opt/spark/work-dir/read_transactions.py

```

# Enriched Transaction Schema

```
    {
  "transaction_id": "uuid",
  "customer_id": "C1234",
  "amount": 45000,
  "currency": "INR",
  "merchant_category": "ECOMMERCE",
  "country": "IN",
  "device_id": "device-12",
  "transaction_time": "2026-03-01T10:15:00Z",

  "hour_of_day": 23,
  "is_high_amount": true,
  "is_night_transaction": true
}
```

# to copy spark job in unix server path

    docker cp streaming/fraud-detection/enrich_transactions.py fraud-spark-master:/opt/spark/work-dir

# to run and see kafka consumer

    /opt/kafka/bin/kafka-console-consumer.sh \

--bootstrap-server kafka:9092 \
 --topic transactions.enriched \
 --from-beginning

#🥇 STAGE 1 — INFRASTRUCTURE SETUP

### We will design enterprise docker-compose running:

- Oracle XE

- Kafka

- Zookeeper

- Spark

- Hadoop

- NiFi
