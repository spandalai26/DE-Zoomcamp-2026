# Module 3 — Step-by-Step Homework Guide

Use this guide in order. Record answers in [homework.md](homework.md).

## Step 1 — Prerequisites
1. Ensure GCP project exists and billing is enabled.
2. Create a GCS bucket (same region you’ll use for BigQuery dataset).
3. Create a BigQuery dataset (note the region).

## Step 2 — Upload data to GCS (Jan–Jun 2024)
1. Download Yellow Taxi parquet files for 2024-01 through 2024-06.
2. Use one loader:
   - Python: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/load_yellow_taxi_data.py
   - DLT notebook: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/DLT_upload_to_GCP.ipynb
3. Verify 6 files exist in your bucket.

## Step 3 — Create external table in BigQuery
1. Create an external table pointing to the parquet files in GCS.
2. Confirm the external table schema is correct.

## Step 4 — Create materialized (regular) table
1. Create a new regular table from the external table.
2. Do not partition or cluster this table.

## Step 5 — Answer Q1–Q4
Use [queries.sql](queries.sql) and paste results into [homework.md](homework.md).

## Step 6 — Partition & cluster table (Q5)
1. Create a partitioned table on `tpep_dropoff_datetime` and clustered on `VendorID`.
2. Record the chosen strategy.

## Step 7 — Answer Q6–Q9
Use the provided queries and record bytes processed and answers.

## Step 8 — Submit
1. Ensure [homework.md](homework.md) has all answers.
2. Submit at https://courses.datatalks.club/de-zoomcamp-2026/homework/hw3

## Reference
- Module overview: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/03-data-warehouse
- Homework: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/homework.md
