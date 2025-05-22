def perform_analysis(df):
    df.groupBy("passenger_count").count().show()
    df.groupBy("payment_type").count().show()