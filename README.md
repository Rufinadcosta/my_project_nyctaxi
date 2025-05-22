# NYC Yellow Taxi Trip Data Analysis

This project analyzes NYC Yellow Taxi trip data using PySpark to uncover insights into trip durations, passenger counts, and temporal patterns.

## Dataset

- Source: [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- Format: Parquet
- Example file: `yellow_tripdata_2023-01.parquet`

## Project Structure

- `data/`: Contains raw data files.
- `notebooks/`: Jupyter notebooks for exploratory data analysis.
- `src/`: Python modules for data ingestion, transformation, and analysis.
- `tests/`: Unit tests for data transformation functions.
- `run_pipeline.py`: Script to execute the data pipeline.

## Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
2. Install dependencies:

   pip install -r requirements.txt

3. Run the data pipeline:

   python run_pipeline.py
