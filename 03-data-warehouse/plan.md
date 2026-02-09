# Module 3 (Data Warehouse & BigQuery) — Completion Plan

## 0) Prerequisites
- [ ] Confirm GCP project + billing enabled
- [ ] Create or verify a GCS bucket for homework data
- [ ] Create a service account with GCS Admin (or be authenticated via gcloud)
- [ ] Set BigQuery dataset location (keep consistent with bucket location)

## 1) Pull and load data (Jan–Jun 2024, Yellow Taxi)
Data source: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Choose one loading method:
- [ ] Python loader: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/load_yellow_taxi_data.py
- [ ] DLT notebook: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/DLT_upload_to_GCP.ipynb

Checklist:
- [ ] Update bucket name in the loader
- [ ] Upload all 6 parquet files (Jan–Jun 2024)
- [ ] Verify the 6 files exist in the bucket

## 2) BigQuery setup
- [ ] Create external table on the GCS parquet files (PARQUET option)
- [ ] Create a materialized (regular) table from the external table (no partition/cluster)

## 3) Homework questions (worklog + answers)
Record answers and query notes as you go.

### Q1 — Count records
- [ ] Run count(*) on the 2024 Yellow Taxi data
- [ ] Record answer choice

### Q2 — Data read estimation
- [ ] Query distinct PULocationID on external table (note bytes)
- [ ] Same query on materialized table (note bytes)
- [ ] Record answer choice

### Q3 — Columnar storage
- [ ] Query only PULocationID on materialized table (note bytes)
- [ ] Query PULocationID + DOLocationID (note bytes)
- [ ] Record explanation choice

### Q4 — Zero fare trips
- [ ] Count rows where fare_amount = 0
- [ ] Record answer choice

### Q5 — Partitioning & clustering
- [ ] Create optimized table for filters on tpep_dropoff_datetime and order by VendorID
- [ ] Record best strategy choice

### Q6 — Partition benefits
- [ ] Query distinct VendorID with date filter on non-partitioned table
- [ ] Query same on partitioned table
- [ ] Record bytes processed and answer choice

### Q7 — External table storage
- [ ] Record where external table data is stored

### Q8 — Clustering best practices
- [ ] Record true/false answer

### Q9 — Table scan understanding (no points)
- [ ] Run SELECT count(*) on materialized table
- [ ] Note estimated bytes and reason

## 4) Submission
- [ ] Prepare a public repo with SQL queries/notes or README answers
- [ ] Submit at https://courses.datatalks.club/de-zoomcamp-2026/homework/hw3

## 5) Optional: learning in public
- [ ] Share a short post (LinkedIn/X) with what you learned

## Reference links
- Module overview: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/03-data-warehouse
- Homework (2026): https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2026/03-data-warehouse/homework.md
- BigQuery SQL basics: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/03-data-warehouse/big_query.sql
- BigQuery ML SQL: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/03-data-warehouse/big_query_ml.sql
- Extract model guide: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/03-data-warehouse/extract_model.md
