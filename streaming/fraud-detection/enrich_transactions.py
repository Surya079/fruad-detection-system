from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import from_json, col, hour, when


# Create spark session to connect master 
spark = SparkSession.builder \
        .appName("TransactionEnrichment") \
        .master("spark://spark-master:7077") \
        .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Input schema to send data to kafka  

schema = StructType(
    [
    StructField("transaction_id", StringType()),
    StructField("customer_id", StringType()),
    StructField("amount", DoubleType()),
    StructField("currency", StringType()),
    StructField("merchant_id", StringType()),
    StructField("merchant_category", StringType()),
    StructField("transaction_type", StringType()),
    StructField("transaction_time", StringType()),
    StructField("country", StringType()),
    StructField("device_id", StringType())
    ]
)

# Read raw topic from kafka

raw_df = spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka:9092") \
            .option("subscribe", "transactions.raw") \
            .option("startingOffsets", "earliest") \
            .load()


# parse the raw data to table

parsed_df = raw_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Enrichment Logic

enriched_df = parsed_df \
                .withColumn("hour_of_day", hour(col("transaction_time"))) \
                .withColumn("is_high_amount", when(col("amount") > 30000, True).otherwise(False)) \
                .withColumn("is_night_transaction", 
                                when((col("hour_of_day") < 6) | (col("hour_of_day") > 22), True).otherwise(False)
                           ) 


# Write to New Kafka topic

query = enriched_df.selectExpr(
    "to_json(struct(*)) AS value"
).writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("topic", "transactions.enriched") \
    .option("checkpointLocation", "/tmp/spark-checkpoints/enriched") \
    .outputMode("append") \
    .start()

query.awaitTermination()

