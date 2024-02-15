import pytest

from assignment1 import heapsort, insertion_sort, merge_sort, quicksort


@pytest.mark.parametrize(
    "unsorted",
    [
        [1],
        [1, 2],
        [2, 1],
        [4, 2, 6],
        [4, 6, 2, 4, 2, 2],
        [4, 6, 2, 5, 6, 7, 4, 2, 5],
    ],
)
def test_insertion_sort(unsorted):
    _sorted = sorted(unsorted)
    insertion_sort(unsorted)
    assert unsorted == _sorted


@pytest.mark.parametrize(
    "unsorted",
    [
        [1],
        [1, 2],
        [2, 1],
        [4, 2, 6],
        [4, 6, 2, 4, 2, 2],
        [4, 6, 2, 5, 6, 7, 4, 2, 5],
    ],
)
def test_merge_sort(unsorted):
    _sorted = sorted(unsorted)
    merge_sort(unsorted, 0, len(unsorted) - 1)
    assert unsorted == _sorted


@pytest.mark.parametrize(
    "unsorted",
    [
        [1],
        [1, 2],
        [2, 1],
        [4, 2, 6],
        [4, 6, 2, 4, 2, 2],
        [4, 6, 2, 5, 6, 7, 4, 2, 5],
    ],
)
def test_heapsort(unsorted):
    _sorted = sorted(unsorted)
    heapsort(unsorted)
    assert unsorted == _sorted


@pytest.mark.parametrize(
    "unsorted",
    [
        [1],
        [1, 2],
        [2, 1],
        [4, 2, 6],
        [4, 6, 2, 4, 2, 2],
        [1, 2, 3, 4, 5],
        [4, 6, 2, 5, 6, 7, 4, 2, 5],
    ],
)
def test_quick_sort(unsorted):
    _sorted = sorted(unsorted)
    quicksort(unsorted, 0, len(unsorted) - 1)
    assert unsorted == _sorted
