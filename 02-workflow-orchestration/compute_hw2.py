import gzip
import urllib.request
from datetime import datetime

BASE_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{taxi}/{file}.csv.gz"


def count_rows_and_size(url: str):
    total_bytes = 0
    rows = 0
    with urllib.request.urlopen(url) as resp:
        with gzip.GzipFile(fileobj=resp) as gz:
            while True:
                chunk = gz.read(1024 * 1024)
                if not chunk:
                    break
                total_bytes += len(chunk)
                rows += chunk.count(b"\n")
    # subtract header row if present
    if rows > 0:
        rows -= 1
    return rows, total_bytes


def month_str(m: int) -> str:
    return f"{m:02d}"


def main():
    results = {}

    # Q1: Yellow 2020-12 uncompressed size
    file_dec = "yellow_tripdata_2020-12"
    url_dec = BASE_URL.format(taxi="yellow", file=file_dec)
    print(f"Downloading and counting: {url_dec}")
    rows_dec, bytes_dec = count_rows_and_size(url_dec)
    results["yellow_2020_12"] = (rows_dec, bytes_dec)

    # Q3: total rows for yellow 2020
    yellow_total = 0
    for m in range(1, 13):
        file_name = f"yellow_tripdata_2020-{month_str(m)}"
        url = BASE_URL.format(taxi="yellow", file=file_name)
        print(f"Downloading and counting: {url}")
        rows, _ = count_rows_and_size(url)
        yellow_total += rows
    results["yellow_2020_total"] = yellow_total

    # Q4: total rows for green 2020
    green_total = 0
    for m in range(1, 13):
        file_name = f"green_tripdata_2020-{month_str(m)}"
        url = BASE_URL.format(taxi="green", file=file_name)
        print(f"Downloading and counting: {url}")
        rows, _ = count_rows_and_size(url)
        green_total += rows
    results["green_2020_total"] = green_total

    # Q5: Yellow 2021-03 rows
    file_2021_03 = "yellow_tripdata_2021-03"
    url_2021_03 = BASE_URL.format(taxi="yellow", file=file_2021_03)
    print(f"Downloading and counting: {url_2021_03}")
    rows_2021_03, _ = count_rows_and_size(url_2021_03)
    results["yellow_2021_03"] = rows_2021_03

    print("\n=== RESULTS ===")
    rows_dec, bytes_dec = results["yellow_2020_12"]
    mib_dec = bytes_dec / (1024 * 1024)
    print(f"Yellow 2020-12 rows: {rows_dec}")
    print(f"Yellow 2020-12 uncompressed size: {bytes_dec} bytes ({mib_dec:.1f} MiB)")
    print(f"Yellow 2020 total rows: {results['yellow_2020_total']}")
    print(f"Green 2020 total rows: {results['green_2020_total']}")
    print(f"Yellow 2021-03 rows: {results['yellow_2021_03']}")


if __name__ == "__main__":
    main()
