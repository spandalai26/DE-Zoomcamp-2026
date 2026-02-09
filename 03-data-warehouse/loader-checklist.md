# Data Loader Checklist (GCS)

## 1) Create bucket
- [ ] Bucket name:
- [ ] Region:
- [ ] Uniform access enabled

## 2) Auth
- [ ] Service account created (GCS Admin) OR gcloud auth login
- [ ] Credentials file path (if using SA):

## 3) Load data
- [ ] Download parquet for 2024-01 to 2024-06
- [ ] Update bucket name in loader
- [ ] Run loader
- [ ] Verify 6 parquet files in GCS

## 4) Notes
- [ ] Parquet option will be used for external table
- [ ] Dataset region matches bucket region
