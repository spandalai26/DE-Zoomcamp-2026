# Module 3 Homework — Worklog & Answers

## Setup notes
- GCP project: project-61a78eb3-826c-415d-ad0
- Dataset: dezoomcamp2026
- GCS bucket: de-zoomcamp-2026
- Service account / auth method:

## External table
- External table name:
- Source files (GCS prefix):
- Table creation notes:

## Materialized table
- Table name:
- Creation notes:

---

## Q1 — Count records
**Query:**

**Result:** 20,332,093

**Answer choice:** 3

## Q2 — Data read estimation (distinct `PULocationID`)
**External table bytes processed:** 0 MB

**Materialized table bytes processed:** 155.12 MB

**Answer choice:** 2

## Q3 — Columnar storage (one vs two columns)
**Bytes for `PULocationID`:** 155.12 MB

**Bytes for `PULocationID`, `DOLocationID`:** 310.24 MB

**Answer choice:** BigQuery is columnar; selecting more columns scans more data.

## Q4 — Zero fare trips
**Result:** 8,333

**Answer choice:** 4

## Q5 — Partitioning and clustering
**Strategy used:** Partition by `tpep_dropoff_datetime` and cluster by `VendorID`

**Answer choice:** 1

## Q6 — Partition benefits
**Non-partitioned bytes processed:** 310.24 MB

**Partitioned bytes processed:** 26.84 MB

**Answer choice:** 2

## Q7 — External table storage
**Answer choice:** GCP Bucket

## Q8 — Clustering best practices
**Answer choice:** False

## Q9 — Table scan understanding (no points)
**Estimated bytes processed:**

**Why:**
