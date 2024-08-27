# Replace Nulls CLI Tool

This command line tool replaces "null" values in a CSV file with 0.

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project root directory.
3. Install the package using `pip`:

    ```sh
    pip install .
    ```

## Usage

To use the command line tool, run the following command:

```sh
replace-nulls-cli-tool <input_file> <output_file>
```
input_file specifies the path of the original file you would like to pass through the script

output_file is the file post-script with the null replacing complete

If you would like to run it against the sample cli-test.csv file in this directory, copy the path of the csv and paste it as the following:

```sh
replace-nulls-cli-tool /path/to/cli-test.csv output.csv
```

## Unit Test

To run the unit tests against the script, run the following command:

```sh
python3 -m unittest test_replace_nulls.py
```
