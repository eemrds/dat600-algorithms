"""Assignment 1 for DAT600 2024."""
from copy import deepcopy
import random
import networkx as nx
import matplotlib.pyplot as plt
import time


def insertion_sort(items: list[int]) -> list[int]:
    """Simple insertion sort algorithm

    Args:
        items: list of ints to be sorted.

    Returns:
        items: list of ints sorted in ascending order.
    """
    for i in range(1, len(items)):
        val = items[i]
        j = i - 1
        while j >= 0 and items[j] > val:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = val
    return items


def merge_sort(items: list[int], left: int, right: int) -> list[int]:
    """Merge sort algorithm.

    Args:
        items: List of items to sort.
        left: Left index of items.
        right: Right index of items.

    Returns:
        List of sorted items.
    """

    def merge(items: list[int], left: int, middle: int, right: int) -> list[int]:
        """Merges two sorted lists into one sorted list.

        Args:
            items: List of items to sort.
            left: Index of leftmost item.
            middle: Index of middle item.
            right: Index of rightmost item.

        Returns:
            Merged sorted list of items.
        """
        n1 = middle - left + 1
        n2 = right - middle
        L = [items[left + i] for i in range(n1)]
        R = [items[middle + i + 1] for i in range(n2)]
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                items[k] = L[i]
                i += 1
            else:
                items[k] = R[j]
                j += 1
            k += 1
        rest = L[i:] if i < n1 else R[j:]
        items[k : k + len(rest)] = rest

    if left < right:
        middle = (left + right) // 2

        merge_sort(items, left, middle)
        merge_sort(items, middle + 1, right)
        merge(items, left, middle, right)


def heapsort(items: list[int]) -> list[int]:
    """Heapsort algorithm.

    Args:
        items: List of items to sort.

    Returns:
        List of sorted items.
    """

    def max_heapify(items: list[int], heapsize: int, i: int) -> None:
        left = lambda: 2 * i + 1
        right = lambda: 2 * i + 2
        largest = i
        if left() < heapsize and items[left()] > items[i]:
            largest = left()
        else:
            largest = i

        if right() < heapsize and items[right()] > items[largest]:
            largest = right()

        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            max_heapify(items, heapsize, largest)

    def build_max_heap(items: list[int], heapsize: int) -> None:
        for i in range(heapsize // 2 - 1, -1, -1):
            max_heapify(items, heapsize, i)

    build_max_heap(items, len(items))

    for i in range(len(items) - 1, 0, -1):
        items[i], items[0] = items[0], items[i]
        max_heapify(items, i, 0)
    return items


def quicksort(items: list[int], left: int, right: int) -> None:
    def partition(items: list[int], left: int, right: int) -> int:
        x = items[right]
        i = left - 1
        for j in range(left, right):
            if items[j] <= x:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[right] = items[right], items[i + 1]
        return i + 1

    if left < right:
        split = partition(items, left, right)
        quicksort(items, left, split - 1)
        quicksort(items, split + 1, right)


if __name__ == "__main__":
    itemsMain = [random.randint(0, 100) for _ in range(10_000)]
    sorting_algorithms = {
        "insertion_sort": (insertion_sort, {}),
        "heapsort": (heapsort, {}),
        "merge_sort": (merge_sort, {"left": 0, "right": len(itemsMain) - 1}),
        "quicksort": (quicksort, {"left": 0, "right": len(itemsMain) - 1}),
    }
    for name, sorted_items in sorting_algorithms.items():
        items = deepcopy(itemsMain)
        params = sorted_items[1]
        params["items"] = items
        func = sorted_items[0]

        start = time.time_ns()
        func(**params)
        end = time.time_ns()
        print(f"Function {name}, time elapsed: {(end - start) / 1000} us.")
        assert items == sorted(deepcopy(items))
