#!/opt/homebrew/bin/python3
import argparse
import csv
import sys
from collections import Counter

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def process_column(values):
    counter = Counter(values)
    most_common, most_common_count = counter.most_common(1)[0]
    #Process a single column, summing or concatenating its values based on data type.
    if not values:
        raise ValueError("Empty column")

    if all(value == "" or is_float(value) for value in values):
        return sum(float(value) for value in values if value != "")
    elif all(value == "" or not is_float(value) for value in values):
        return {
            "unique_values": len(counter),
            "most_common": most_common,
            "frequency_of_most_common": most_common_count,
            "all_frequencies": dict(counter)
        }
    else:
        raise ValueError("Mixed data types in column")

def process_csv(reader, target_column=None):
    #Process the CSV and compute the result for the specified column or all columns.
    headers = next(reader)
    columns = {header: [] for header in headers}
    
    for row in reader:
        for header, value in zip(headers, row):
            columns[header].append(value)

    if target_column:
        if target_column not in columns:
            raise ValueError(f"Column '{target_column}' not found in CSV")
        return {target_column: process_column(columns[target_column])}
    else:
        results = {}
        for header, values in columns.items():
            results[header] = process_column(values)
        return results

def main():
    parser = argparse.ArgumentParser(description="Sum and concatenate CSV file columns.")
    parser.add_argument('filename', help="CSV file to process")
    parser.add_argument('--column', help="Specific column to process", default=None)
    args = parser.parse_args()

    try:
        if args.filename.endswith(".csv"):
            with open(args.filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                results = process_csv(reader, args.column)
                for header, result in results.items():
                    print(f"{header}: {result}")
        else:
            raise ValueError("The file is not a CSV")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
