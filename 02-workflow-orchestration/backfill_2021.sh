#!/bin/bash

# Backfill script for Kestra PostgreSQL taxi flow
# Loads 2021 data (January - July) for both yellow and green taxi

BASE_URL="http://localhost:8080"
USER="admin@kestra.io"
PASS="Admin1234!"

# Function to trigger a flow with inputs
trigger_flow() {
  local taxi=$1
  local year=$2
  local month=$3
  
  echo "Triggering execution: taxi=$taxi, year=$year, month=$month"
  
  curl -u "$USER:$PASS" -X POST "$BASE_URL/api/v1/executions/trigger/zoomcamp/05_postgres_taxi_scheduled?inputs%5Btaxi%5D=$taxi&inputs%5Byear%5D=$year&inputs%5Bmonth%5D=$month"
  
  echo ""
  sleep 2
}

# Backfill 2021 green taxi data (Jan-Jul)
echo "=== Backfilling Green Taxi 2021 Data ==="
for month in 01 02 03 04 05 06 07; do
  trigger_flow "green" "2021" "$month"
done

# Backfill 2021 yellow taxi data (Jan-Jul)
echo ""
echo "=== Backfilling Yellow Taxi 2021 Data ==="
for month in 01 02 03 04 05 06 07; do
  trigger_flow "yellow" "2021" "$month"
done

echo ""
echo "All backfill executions have been triggered!"
echo "Check Kestra UI at $BASE_URL/ui/main to monitor progress."
