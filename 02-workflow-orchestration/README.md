# Week 2: Workflow Orchestration with Kestra

## Setup Instructions

### Prerequisites
- Docker and Docker Compose installed
- Google Cloud account (for GCP section)

### Starting Kestra

```bash
cd 02-workflow-orchestration
docker compose up -d
```

Once started, access:
- **Kestra UI**: http://localhost:8080
  - Username: `admin@kestra.io`
  - Password: `Admin1234!`
- **pgAdmin**: http://localhost:8085
  - Email: `admin@admin.com`
  - Password: `root`

### Stopping Kestra

```bash
docker compose down
```

## Course Structure

### 2.1 Introduction to Workflow Orchestration
- What is workflow orchestration?
- Introduction to Kestra

### 2.2 Getting Started with Kestra
- Installing Kestra with Docker Compose
- Kestra concepts (Flows, Tasks, Inputs, Outputs, Triggers, etc.)
- Orchestrating Python code

### 2.3 Hands-On: Build ETL Data Pipelines
- Getting started pipeline
- Load taxi data to Postgres
- Scheduling and backfills

### 2.4 ELT Pipelines with Google Cloud Platform
- ETL vs ELT
- Setup GCP (Service Account, GCS, BigQuery)
- Load taxi data to BigQuery
- Schedule and backfill full dataset

### 2.5 Using AI for Data Engineering
- Context engineering with ChatGPT
- AI Copilot in Kestra
- RAG (Retrieval Augmented Generation)

## Homework Assignment

### Task
Extend existing flows to include data for **2021** (January - July) for both Yellow and Green taxi data.

### Quiz Questions
1. File size for Yellow Taxi Dec 2020
2. Rendered variable value
3. Yellow taxi row count for 2020
4. Green taxi row count for 2020
5. Yellow taxi row count for March 2021
6. Timezone configuration

### Approach
- Use backfill functionality in scheduled flow
- Time period: `2021-01-01` to `2021-07-31`
- Process both `yellow` and `green` taxi services

## Resources

- [Kestra Documentation](https://kestra.io/docs)
- [YouTube Playlist](https://go.kestra.io/de-zoomcamp/yt-playlist)
- [Course GitHub](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration)
- [Kestra Slack](https://kestra.io/slack)

## Notes

### Docker Compose Configuration
- **Postgres** for NY Taxi data (port 5432)
- **pgAdmin** for database management (port 8085)
- **Kestra Postgres** for Kestra metadata
- **Kestra** server (ports 8080, 8081)

### Important Commands
```bash
# Start services
docker compose up -d

# Stop services
docker compose down

# View logs
docker compose logs -f kestra

# Restart Kestra only
docker compose restart kestra
```

## Troubleshooting

- Ensure port 8080 is not in use by other services
- Pin Kestra image to `kestra/kestra:v1.1` (not `develop`)
- Use Postgres 18 image
- If issues persist, stop containers and restart: `docker compose down && docker compose up -d`
