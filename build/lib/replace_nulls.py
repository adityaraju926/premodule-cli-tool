import csv
import argparse

def replace_nulls_in_csv(input_file, output_file):
    with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            new_row = [0 if cell.lower() == 'null' else cell for cell in row]
            writer.writerow(new_row)

def main():
    parser = argparse.ArgumentParser(description='Replace "null" values in a CSV file with 0.')
    parser.add_argument('input_file', type=str, help='Path to the input CSV file')
    parser.add_argument('output_file', type=str, help='Path to the output CSV file')
    args = parser.parse_args()
    
    replace_nulls_in_csv(args.input_file, args.output_file)
    print(f'"null" values in {args.input_file} have been replaced with 0 and saved to {args.output_file}')

if __name__ == "__main__":
    main()