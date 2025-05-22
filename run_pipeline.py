from src import data_ingestion, data_transformation, data_analysis

def main():
    spark = data_ingestion.create_spark_session()
    df = data_ingestion.load_data(spark, 'data/raw/yellow_tripdata_2023-01.parquet')
    transformed_df = data_transformation.transform_data(df)
    data_analysis.perform_analysis(transformed_df)

if __name__ == "__main__":
    main()