import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from algorithms.mergeSort import merge_sort  # type: ignore
from tests.fixtures import dummy_data, output_data  # noqa: F401


class TestMergeSort:
    def test_sort(self):
        data = [2, 4, 8, 6]
        assert merge_sort(data) == [2, 4, 6, 8]

    def test_reversed_sort(self):
        data = [2, 4, 8, 6]
        assert merge_sort(data, reversed=True) == [8, 6, 4, 2]

    def test_key_sort(self):
        data = [2, 4, 8, 6]
        assert merge_sort(data, key=lambda x: -x) == [8, 6, 4, 2]

    def test_key_reversed_sort(self):
        data = [2, 4, 8, 6]
        assert merge_sort(data, key=lambda x: -x, reversed=True) == [2, 4, 6, 8]

    def test_stable_sort(self):
        data = [2, 4, 8, 6]
        assert merge_sort(data, key=lambda x: x % 2) == [2, 4, 8, 6]

    def test_dummy_data(self, dummy_data, output_data):  # noqa: F811
        assert merge_sort(dummy_data, key=lambda x: x[0]) == output_data


if __name__ == "__main__":
    import pytest

    pytest.main()
