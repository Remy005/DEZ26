import sys

print("arguments", sys.argv)

# Use default day if not provided
if len(sys.argv) > 1:
    try:
        day = int(sys.argv[1])
    except ValueError:
        print(f"Error: '{sys.argv[1]}' is not a valid integer")
        day = 1  # Default to day 1cd
else:
    day = 1  # Default to day 1

print(f"Running pipeline for day {day}")