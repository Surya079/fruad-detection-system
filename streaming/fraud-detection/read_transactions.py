from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import from_json, col


# Creating Spark Session to connect master

spark = SparkSession.builder \
            .appName("TransactionStreamReader") \
            .master("spark://spark-master:7077") \
            .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define Schema (same we mentioned in NiFi)

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

# Read from Kafka  (Consumer)

raw_df = spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", "kafka:9092") \
            .option("subscribe", "transactions.raw") \
            .option("startingOffsets", "earliest") \
            .load()

# Converting Kafka value to table col format 

parsed_df = raw_df \
    .select(
        from_json(col("value").cast("string"), schema).alias("data")
    ).select("data.*")

query = parsed_df.writeStream \
           .format("console") \
           .outputMode("append") \
           .option("truncate", "false") \
           .start()

query.awaitTermination()


