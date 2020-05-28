import csv


def get_csv_data(file_name):

    # Create empty list to store rows
    rows = []

    # Open the CSV file
    data_file = open(file_name, 'r')

    # Create a CSV reader from CSV file
    reader_of_file = csv.reader(data_file)

    # skip the headers - don tread the first row
    next(reader_of_file)

    # add rows from reader to list
    for row in reader_of_file:
        rows.append(row)

    return rows
