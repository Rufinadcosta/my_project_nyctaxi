from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder.appName("NYC Taxi Analysis").getOrCreate()

def load_data(spark, file_path):
    return spark.read.parquet(file_path)