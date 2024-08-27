import unittest
import csv
from replace_nulls import replace_nulls_in_csv

class TestReplaceNulls(unittest.TestCase):
    
    def test_replace_nulls_in_csv(self):
        # Mock csv struct with null values to pass into script
        with open('test_input.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Salary'])
            writer.writerow(['Aditya', 'null', '100000'])
            writer.writerow(['Paul', '30', 'null'])
            writer.writerow(['Gavin', 'null', '80000'])
        
        # Run the replace_nulls_in_csv function
        replace_nulls_in_csv('test_input.csv', 'test_output.csv')
        
        # Asserting output with expected output from script
        with open('test_output.csv', mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(rows[1], ['Aditya', '0', '100000'])
            self.assertEqual(rows[2], ['Paul', '30', '0'])
            self.assertEqual(rows[3], ['Gavin', '0', '80000'])

if __name__ == '__main__':
    unittest.main()