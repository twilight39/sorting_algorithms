import pytest
import csv
import os

CSV_DUMMY_FILE_PATH = os.path.join(os.path.dirname(__file__), "dummy_data.csv")
CSV_OUTPUT_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "../output/name_ascending.csv"
)


@pytest.fixture
def dummy_data() -> list[list[str]]:
    data_list = []
    with open(CSV_DUMMY_FILE_PATH, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            data_list.append(row)

    data_list.pop(0)
    return data_list


@pytest.fixture
def output_data() -> list[list[str]]:
    data_list = []
    with open(CSV_OUTPUT_FILE_PATH, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            data_list.append(row)

    data_list.pop(0)
    return data_list
