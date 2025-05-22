from pyspark.sql.functions import col, to_timestamp

def transform_data(df):
    df = df.withColumn("pickup_datetime", to_timestamp(col("tpep_pickup_datetime")))
    df = df.withColumn("dropoff_datetime", to_timestamp(col("tpep_dropoff_datetime")))
    df = df.filter(col("passenger_count") > 0)
    return df