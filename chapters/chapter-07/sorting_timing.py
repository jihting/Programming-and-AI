"""Timing starter for Week 3 Lab 1.

Copy this into your week-3 folder as sorting_timing.py.
You will connect it to your own merge_sort implementation during the lab.
"""

import random
import time


def make_random_list(size):
    return [random.randint(1, size * 10) for _ in range(size)]


def time_function(function, values):
    start = time.perf_counter()
    result = function(values)
    end = time.perf_counter()
    return result, end - start


# Replace this with: from merge_sort import merge_sort
# when your merge_sort.py file is ready.
def placeholder_sort(values):
    return sorted(values)


if __name__ == "__main__":
    sizes = [10, 100, 1000]

    for size in sizes:
        values = make_random_list(size)

        own_result, own_time = time_function(placeholder_sort, values.copy())
        built_in_result, built_in_time = time_function(sorted, values.copy())

        assert own_result == built_in_result

        print(f"Size: {size}")
        print(f"  Your sort: {own_time:.6f} seconds")
        print(f"  sorted():  {built_in_time:.6f} seconds")
        print()
