from math import log2
import random
from matplotlib import pyplot as plt


def insertion_sort_steps(items: list[int]) -> int:
    """Modified insertion sort to count steps."""
    step_counter = 0
    for i in range(1, len(items)):
        val = items[i]
        j = i - 1
        step_counter += 2
        while j >= 0 and items[j] > val:
            items[j + 1] = items[j]
            j -= 1
            step_counter += 2
        items[j + 1] = val
    return step_counter


def merge_sort_steps(items, left, right):
    """Modified merge sort to count steps."""
    global step_counter

    def merge(items, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle
        L = [items[left + i] for i in range(n1)]
        R = [items[middle + 1 + i] for i in range(n2)]
        step_counter += n1 + n2
        i, j, k = 0, 0, left
        while i < n1 and j < n2:
            step_counter += 1
            if L[i] <= R[j]:
                items[k] = L[i]
                i += 1
            else:
                items[k] = R[j]
                j += 1
            k += 1
            step_counter += 1
        while i < n1:
            items[k] = L[i]
            i += 1
            k += 1
            step_counter += 1
        while j < n2:
            items[k] = R[j]
            j += 1
            k += 1
            step_counter += 1

    if left < right:
        middle = (left + right) // 2
        merge_sort_steps(items, left, middle)
        merge_sort_steps(items, middle + 1, right)
        merge(items, left, middle, right)


def heapsort_steps(items):
    global step_counter

    def max_heapify(items, heapsize, i):
        global step_counter
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < heapsize and items[left] > items[i]:
            largest = left
            step_counter += 1
        if right < heapsize and items[right] > items[largest]:
            largest = right
            step_counter += 1
        if largest != i:
            items[i], items[largest] = items[largest], items[i]
            step_counter += 1
            max_heapify(items, heapsize, largest)

    def build_max_heap(items):
        heapsize = len(items)
        for i in range(heapsize // 2 - 1, -1, -1):
            max_heapify(items, heapsize, i)

    build_max_heap(items)
    for i in range(len(items) - 1, 0, -1):
        items[i], items[0] = items[0], items[i]
        step_counter += 1
        max_heapify(items, i, 0)


def quicksort_steps(items, left, right):
    global step_counter

    def partition(items, left, right):
        global step_counter
        pivot = items[right]
        i = left - 1
        for j in range(left, right):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
                step_counter += 1
        items[i + 1], items[right] = items[right], items[i + 1]
        step_counter += 1
        return i + 1

    if left < right:
        pi = partition(items, left, right)
        quicksort_steps(items, left, pi - 1)
        quicksort_steps(items, pi + 1, right)


def plot_sort_steps(lists, func):
    fig, ax = plt.subplots(1, 2)
    fig.suptitle("Counted steps and Asymptotic running time")

    for num, B in enumerate(lists):
        points = 8
        x = []
        y = []
        ref = []
        c = []

        for i in range(0, points):
            print(i + 1, "/", points)
            steps = func(B.copy())
            B = B * 2
            x.append(len(B))
            y.append(steps)
            c.append(steps / len(B) ** 2)

        median_index = len(c) - 1

        for v in x:
            ref.append(v**2 * c[median_index])
        ax[0].plot(
            x,
            ref,
            linestyle="-",
            label=f"{num+1}: {round(c[median_index], 2)}.n^2 --> O(n^2)",
        )
        ax[0].plot(x, y, label=f"{num + 1}: counted steps")
        ax[0].set_xlabel("size of n")
        ax[0].set_ylabel("computation steps")
        ax[0].legend()

        ax[1].scatter(x, c, label="approximation of c")
        ax[1].set_xlabel("size of n")
        ax[1].set_ylabel("c factor")
        ax[1].legend()
    plt.show()


lists = [
    [random.randint(1, 10) for _ in range(random.randint(10, 10))] for _ in range(1)
]

plot_sort_steps(lists, insertion_sort_steps)


# insertion_sort_steps = measure_performance(insertion_sort_steps, input_sizes)

# actual_insertion_sort_steps = [insertion_sort_steps(list_) for list_ in input_sizes]
# actual_merge_sort_steps = [
#     merge_sort_steps(list_, 0, len(list_) - 1) for list_ in input_sizes
# ]


# theoretical_insertion_sort_steps = [
#     estimated_insertion_sort_steps(len(list_)) for list_ in input_sizes
# ]
# theoretical_merge_sort_steps = [
#     estimated_merge_sort_steps(len(list_)) for list_ in input_sizes
# ]

# input_lengths = [len(list_) for list_ in input_sizes]

# plt.scatter(
#     input_lengths,
#     actual_insertion_sort_steps,
#     color="blue",
#     label="Actual Steps",
#     alpha=0.7,
# )
# plt.plot(
#     input_lengths,
#     theoretical_insertion_sort_steps,
#     color="red",
#     label="Estimated Steps",
# )
# plt.title("Insertion Sort Performance")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Number of Steps")
# plt.legend()
# plt.grid(True)
# plt.show()

# plt.scatter(
#     input_lengths,
#     actual_merge_sort_steps,
#     color="green",
#     label="Actual Steps",
#     alpha=0.7,
# )
# plt.plot(
#     input_lengths,
#     theoretical_merge_sort_steps,
#     color="red",
#     label="Estimated Steps",
#     linestyle="--",
# )
# plt.title("Merge Sort Performance")
# plt.xlabel("Input Size (n)")
# plt.ylabel("Number of Steps")
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()
# print("Done!")
