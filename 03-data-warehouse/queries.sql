-- Module 3 Homework Queries (fill in project/dataset/table names)

-- Step A: Create external table
-- CREATE OR REPLACE EXTERNAL TABLE `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.external_table`
-- OPTIONS (
--   format = 'PARQUET',
--   uris = ['gs://de-zoomcamp-2026/yellow_tripdata_2024-0*.parquet']
-- );

-- Step B: Create materialized (regular) table (no partition/cluster)
-- CREATE OR REPLACE TABLE `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table` AS
-- SELECT * FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.external_table`;

-- Q1: Count records
-- SELECT COUNT(*) AS total_records
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`;

-- Q2: Distinct PULocationID on external table
-- SELECT COUNT(DISTINCT PULocationID) AS distinct_pu
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.external_table`;

-- Q2: Distinct PULocationID on materialized table
-- SELECT COUNT(DISTINCT PULocationID) AS distinct_pu
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`;

-- Q3: Columnar storage (one column)
-- SELECT PULocationID
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`;

-- Q3: Columnar storage (two columns)
-- SELECT PULocationID, DOLocationID
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`;

-- Q4: Zero fare trips
-- SELECT COUNT(*) AS zero_fare_trips
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`
-- WHERE fare_amount = 0;

-- Q5: Partition + clustering table creation
-- CREATE OR REPLACE TABLE `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.partitioned_clustered_table`
-- PARTITION BY DATE(tpep_dropoff_datetime)
-- CLUSTER BY VendorID AS
-- SELECT *
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`;

-- Q6: Distinct VendorID between dates (non-partitioned)
-- SELECT DISTINCT VendorID
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`
-- WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

-- Q6: Distinct VendorID between dates (partitioned table)
-- SELECT DISTINCT VendorID
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.partitioned_clustered_table`
-- WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';

-- Q9: Table scan understanding (no points)
-- SELECT COUNT(*)
-- FROM `project-61a78eb3-826c-415d-ad0.dezoomcamp2026.materialized_table`;
