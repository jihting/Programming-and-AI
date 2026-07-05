"""Starter code for Week 3 Lab 1: merge sort.

Copy this file into your own week-3 folder and rename it to merge_sort.py.
Complete the TODO sections during the lab.
"""


def merge(left, right):
    """Return one sorted list containing the items from two sorted lists."""
    result = []
    i = 0
    j = 0

    # TODO: compare the front item from each list while both lists have items left.
    # Append the smaller item to result and move the matching index forward.

    # TODO: append any remaining items from left and right.

    return result


def merge_sort(values):
    """Return a sorted copy of values using recursive merge sort."""
    # TODO: base case: a list of length 0 or 1 is already sorted.

    # TODO: split the list in half.

    # TODO: sort each half recursively.

    # TODO: merge the two sorted halves.
    return values


if __name__ == "__main__":
    # UNCOMMENT when merge() is complete:
# assert merge([1, 4], [2, 3]) == [1, 2, 3, 4]
    assert merge_sort([]) == []
    assert merge_sort([5]) == [5]
    assert merge_sort([3, 1, 2]) == [1, 2, 3]
    print("Merge sort checks passed")
