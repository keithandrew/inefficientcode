# import libraries for CLI and csv files
import argparse
import csv

# set up the CLI
parser = argparse.ArgumentParser(description="Fix csv file")
parser.add_argument("source", type=str, help="Source CSV file for cleaning")
parser.add_argument("output", type=str, help="Cleaned CSV file for output")

args = parser.parse_args()

# test the CLI
print(args.source)
print(args.output)

# open a csv file and print test output
with open(args.source) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print(args.output)
