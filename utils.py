import csv
import itertools
import json


# file_name, row_count
def csv_to_json(file_name, row_count):
    data = []
    headings = []

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # get num of columns
        cols = len(next(csv_reader))

        csv_file.seek(0)

        line_count = 0

        for row in csv_reader:  # for each row
            if line_count == 0:  # if first row
                for i in range(cols):  # loop through elements of row adding to headings array
                    headings.append(row[i])
            else:  # if not first row
                if line_count <= row_count:  # if current line less than max lines
                    json_obj = {}
                    for i in range(cols):  # create dict object pairing col_heading to row_data
                        json_obj.update({headings[i]: row[i]})

                    data.append(json_obj)  # append the dict to the json array
                    del json_obj

            line_count += 1

        print(data[0])

    return data
