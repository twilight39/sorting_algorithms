import csv
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort


def read_csv(file_path):
    data_list = []
    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            data_list.append(row)

    header = data_list.pop(0)
    return header, data_list


def write_csv(file_path, header, data_list):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_list)


if __name__ == "__main__":
    import os

    DUMMY_CSV_FILE_PATH = os.path.join(
        os.path.dirname(__file__), "tests/dummy_data.csv"
    )
    OUTPUT_CSV_FILE_PATH = os.path.join(
        os.path.dirname(__file__), "output/output_data.csv"
    )

    header, data = read_csv(DUMMY_CSV_FILE_PATH)
    write_csv(
        OUTPUT_CSV_FILE_PATH,
        header,
        merge_sort(data, key=lambda x: x[2], reversed=True),
    )
