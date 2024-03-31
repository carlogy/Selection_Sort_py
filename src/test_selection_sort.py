import unittest

from selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    def test_reverse_order_list(self):
        array = [10,9,8,7,6,5,4,3,2,1]
        sorted = [1,2,3,4,5,6,7,8,9,10]
        self.assertListEqual(
            sorted,
            selection_sort(array)
        )

    def test_sorted_list(self):
        array = [0,1,2,3,4,5,6,7,8,9,10]
        self.assertListEqual(
            list(range(0,11)),
            selection_sort(array)
        )

    def test_empty_list(self):
        array = []
        self.assertListEqual(
            [],
            selection_sort(array)
        )

if __name__ == '__main__':
    unittest.main()
