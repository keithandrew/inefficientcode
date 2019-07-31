# import libraries for CLI and csv files
import argparse
import csv

# set up the CLI
parser = argparse.ArgumentParser(description="Fix csv file")
parser.add_argument("source", type=str, help="Source CSV file for cleaning")
parser.add_argument("output", type=str, help="Cleaned CSV file for output")
parser.add_argument('--in-delimiter', type=str, help="Manually specify delimiter")
parser.add_argument('--in-quote', type=str, help="Manually specify delimiter")
args = parser.parse_args()

# open a csv file and print test output
with open(args.source) as csvfile:

    arguments = {}

    if args.in_delimiter:
        arguments["delimiter"] = args.in_delimiter

    if args.in_quote:
        arguments["quotechar"] = args.in_quote

    # if no delimiter or quote specified, then sniff the file and return dialect
    if not args.in_delimiter and not args.in_quote:
        arguments["dialect"] = csv.Sniffer().sniff(csvfile.read())
        csvfile.seek(0)

    reader = csv.reader(csvfile, **arguments)

    # write new csv file
    with open(args.output, "w", newline="") as csv_output:
        writer = csv.writer(csv_output)
        writer.writerows(row for row in reader)
