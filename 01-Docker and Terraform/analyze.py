import pandas as pd
import pyarrow.parquet as pq

# Load the data
df = pd.read_parquet('green_tripdata_2025-11.parquet')
zones = pd.read_csv('taxi_zone_lookup.csv')

# Convert lpep_pickup_datetime to datetime if needed
df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime'])
df['pickup_date'] = df['lpep_pickup_datetime'].dt.date

print("=" * 60)
print("QUESTION 3: Trips with distance <= 1 mile in Nov 2025")
print("=" * 60)

# Filter for trips with distance <= 1 mile
short_trips = df[df['trip_distance'] <= 1]
q3_answer = len(short_trips)
print(f"\nNumber of trips with trip_distance <= 1 mile: {q3_answer:,}")
print(f"Options: 7,853 / 8,007 / 8,254 / 8,421")

print("\n" + "=" * 60)
print("QUESTION 4: Longest trip by pickup day (distance < 100)")
print("=" * 60)

# Filter for trips < 100 miles
valid_trips = df[df['trip_distance'] < 100].copy()

# Group by pickup date and find max distance per day
daily_longest = valid_trips.groupby('pickup_date')['trip_distance'].max().reset_index()
daily_longest = daily_longest.sort_values('trip_distance', ascending=False)

print("\nTop 5 days by longest trip distance:")
print(daily_longest.head())

q4_date = daily_longest.iloc[0]['pickup_date']
q4_distance = daily_longest.iloc[0]['trip_distance']
print(f"\nAnswer: {q4_date} with {q4_distance} miles")

print("\n" + "=" * 60)
print("QUESTION 5: Largest total_amount by pickup zone on Nov 18")
print("=" * 60)

# Filter for Nov 18, 2025
nov_18_trips = df[df['pickup_date'] == pd.to_datetime('2025-11-18').date()]
print(f"\nTrips on Nov 18: {len(nov_18_trips)}")

# Group by PULocationID and sum total_amount
zone_totals = nov_18_trips.groupby('PULocationID')['total_amount'].sum().reset_index()
zone_totals = zone_totals.sort_values('total_amount', ascending=False)

# Merge with zone names
zone_totals = zone_totals.merge(zones, left_on='PULocationID', right_on='LocationID', how='left')

print("\nTop 5 zones by total_amount on Nov 18:")
print(zone_totals[['PULocationID', 'Zone', 'total_amount']].head())

q5_zone = zone_totals.iloc[0]['Zone']
q5_amount = zone_totals.iloc[0]['total_amount']
print(f"\nAnswer: {q5_zone} with ${q5_amount:,.2f}")

print("\n" + "=" * 60)
print("QUESTION 6: Largest tip from East Harlem North pickups")
print("=" * 60)

# Find LocationID for "East Harlem North"
east_harlem_north_id = zones[zones['Zone'] == 'East Harlem North']['LocationID'].values
if len(east_harlem_north_id) > 0:
    east_harlem_north_id = east_harlem_north_id[0]
    print(f"\nEast Harlem North LocationID: {east_harlem_north_id}")
    
    # Filter trips picked up from East Harlem North in November
    ehn_trips = df[(df['PULocationID'] == east_harlem_north_id) & (df['pickup_date'] >= pd.to_datetime('2025-11-01').date())]
    print(f"Trips from East Harlem North in Nov: {len(ehn_trips)}")
    
    # Group by dropoff zone and find max tip
    dropoff_tips = ehn_trips.groupby('DOLocationID')['tip_amount'].max().reset_index()
    dropoff_tips = dropoff_tips.sort_values('tip_amount', ascending=False)
    
    # Merge with zone names
    dropoff_tips = dropoff_tips.merge(zones, left_on='DOLocationID', right_on='LocationID', how='left')
    
    print("\nTop 5 dropoff zones by max tip from East Harlem North:")
    print(dropoff_tips[['DOLocationID', 'Zone', 'tip_amount']].head())
    
    q6_zone = dropoff_tips.iloc[0]['Zone']
    q6_tip = dropoff_tips.iloc[0]['tip_amount']
    print(f"\nAnswer: {q6_zone} with ${q6_tip} tip")
else:
    print("East Harlem North not found in zones data")
