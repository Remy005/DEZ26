import sys

print("arguments", sys.argv)
import pandas as pd

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

# Check if argument was provided
if len(sys.argv) < 2:
    print("Error: Please provide a day number")
    print("Usage: python pipeline.py <day_number>")
    sys.exit(1)  # Exit with error code

try:
    day = int(sys.argv[1])
    print(f"Running pipeline for day {day}")
except ValueError:
    print(f"Error: '{sys.argv[1]}' is not a valid integer")
    sys.exit(1)

