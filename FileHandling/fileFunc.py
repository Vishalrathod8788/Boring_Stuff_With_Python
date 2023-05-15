import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./run.py <path to .csv file>")
        sys.exit(1)

    
    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print("File not found")
        sys.exit(1)
        print("Reading file {}".format(csv_path))
        # Reading csv file
        # TODO: Read csv file
        # print(csv_data)
        # print("Reading csv file {}".format(csv_path))

        # print(csv_data)
        # print(csv_data.head())
        # print(csv_data.tail())
        # print(csv_data.info())
        # print(csv_data.describe())
        