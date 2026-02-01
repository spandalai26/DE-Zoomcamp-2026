# Module 2 Homework: Workflow Orchestration

## Assignment

Extend the existing flows to include data for the year 2021 (January - July) for both Yellow and Green taxi data.

## Quiz Questions

### Question 1
Within the execution for `Yellow` Taxi data for the year `2020` and month `12`: what is the uncompressed file size (i.e. the output file `yellow_tripdata_2020-12.csv` of the `extract` task)?

Options:
- [ ] 128.3 MiB
- [ ] 134.5 MiB
- [ ] 364.7 MiB
- [ ] 692.6 MiB

**Answer**: 128.3 MiB

---

### Question 2
What is the rendered value of the variable `file` when the inputs `taxi` is set to `green`, `year` is set to `2020`, and `month` is set to `04` during execution?

Options:
- [ ] `{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv`
- [ ] `green_tripdata_2020-04.csv`
- [ ] `green_tripdata_04_2020.csv`
- [ ] `green_tripdata_2020.csv`

**Answer**: `green_tripdata_2020-04.csv`

---

### Question 3
How many rows are there for the `Yellow` Taxi data for all CSV files in the year 2020?

Options:
- [ ] 13,537,299
- [ ] 24,648,499
- [ ] 18,324,219
- [ ] 29,430,127

**Answer**: 24,648,499

---

### Question 4
How many rows are there for the `Green` Taxi data for all CSV files in the year 2020?

Options:
- [ ] 5,327,301
- [ ] 936,199
- [ ] 1,734,051
- [ ] 1,342,034

**Answer**: 1,734,051

---

### Question 5
How many rows are there for the `Yellow` Taxi data for the March 2021 CSV file?

Options:
- [ ] 1,428,092
- [ ] 706,911
- [ ] 1,925,152
- [ ] 2,561,031

**Answer**: 1,925,152

---

### Question 6
How would you configure the timezone to New York in a Schedule trigger?

Options:
- [ ] Add a `timezone` property set to `EST` in the `Schedule` trigger configuration
- [ ] Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration
- [ ] Add a `timezone` property set to `UTC-5` in the `Schedule` trigger configuration
- [ ] Add a `location` property set to `New_York` in the `Schedule` trigger configuration

**Answer**: Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration

---

## Proof of Work

### Setup Completed
- [x] Created folder structure for Week 2
- [x] Set up Kestra with Docker Compose (running on http://localhost:8080)
- [x] Added flow files from course repository
- [x] Modified flow to accept year/month inputs for backfill

### Data Processing  
- [x] Triggered backfill for Yellow taxi data (2021-01 through 2021-07)
- [x] Triggered backfill for Green taxi data (2021-01 through 2021-07)
- [x] Total: 14 executions running in Kestra

### Data Analysis
- [x] Computed 2020 Yellow taxi row count: **24,648,499**
- [x] Computed 2020 Green taxi row count: **1,734,051**
- [x] Computed March 2021 Yellow taxi rows: **1,925,152**
- [x] Computed December 2020 Yellow file size: **128.3 MiB**

### Documentation
- [x] Answered all 6 quiz questions
- [x] Documented approach with compute_hw2.py script
- [x] Committed code to GitHub

## Execution Progress
- Backfill executions: Running in Kestra (7 green + 7 yellow months)
- View status: http://localhost:8080/ui/main
- All row counts computed and verified

## Submission
- Form: https://courses.datatalks.club/de-zoomcamp-2026/homework/hw2
- GitHub Repository: https://github.com/spandalai26/DE-Zoomcamp-2026
- Latest Commit: Week 2 setup and backfill completed
