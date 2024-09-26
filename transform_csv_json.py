import csv
import json
import argparse


"""Transform CSV to JSON 
Keyword arguments: source_file output_filename
csv_file_path: csv input path
json_file_path: json output path
Return: None
TODO:  Make it return a dictionary with status - for automation

Usage example: python script.py input.csv output.json

"""

def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Open and read the CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Convert each row into a dictionary and add it to the data list
        for row in csv_reader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

    print(f"CSV content has been written to {json_file_path}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Convert a CSV file to a JSON file.')
    parser.add_argument('csv_file', type=str, help='Path to the input CSV file.')
    parser.add_argument('json_file', type=str, help='Path to the output JSON file.')

    args = parser.parse_args()

    # Call the csv_to_json function with parsed arguments
    csv_to_json(args.csv_file, args.json_file)

if __name__ == "__main__":
    main()
