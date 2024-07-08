import csv
from algorithms.bubbleSort import bubble_sort

def read_csv(file_path):
    data_list = []
    with open(csv_file_path, 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            data_list.append(row)

    header = data_list.pop(0)
    return header, data_list

def write_csv(file_path, header, data_list):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_list)


if __name__ == '__main__':
    csv_file_path = 'tests/dummy_data.csv'
    output_file_path = 'output/output_data.csv'

    header, data = read_csv(csv_file_path)
    write_csv(output_file_path, header, bubble_sort(data, index=0))
    