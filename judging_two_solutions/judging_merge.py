from typing import List

def merge_lists_best(list1: List[int], list2: List[int]) -> List[int]:
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result += list1[i:]
    result += list2[j:]
    return result

def merge_lists_simple(list1: List[int], list2: List[int]) -> List[int]:
    return sorted(list1 + list2)

def test():
    print("Running tests")

    assert merge_lists_best([8], [4, 6, 13]) == [4, 6, 8, 13]
    assert merge_lists_simple([8], [4, 6, 13]) == [4, 6, 8, 13]

    assert merge_lists_best([], [1, 2, 4]) == [1, 2, 4]
    assert merge_lists_simple([], [1, 2, 4]) == [1, 2, 4]

    assert merge_lists_best([1, 2, 4], []) == [1, 2, 4]
    assert merge_lists_simple([1, 2, 4], []) == [1, 2, 4]

    assert merge_lists_best([], []) == []
    assert merge_lists_simple([], []) == []

    assert merge_lists_best([2], [1]) == [1, 2]
    assert merge_lists_simple([2], [1]) == [1, 2]

    assert merge_lists_best([-1, 5, 8], [2, 6, 10]) == [-1, 2, 5, 6, 8, 10]
    assert merge_lists_simple([-1, 5, 8], [2, 6, 10]) == [-1, 2, 5, 6, 8, 10]

    assert merge_lists_best([-1, 5, 8], [5, 8, 10]) == [-1, 5, 5, 8, 8, 10]
    assert merge_lists_simple([-1, 5, 8], [5, 8, 10]) == [-1, 5, 5, 8, 8, 10]

    print("merge_lists_best() with unsorted input: ", merge_lists_best([3, 1], [2]))
    # the above is used to illustrate how merge_lists_best() doesn't work if 
    # either of the input lists are unsorted. Here print is used instead of 
    # assert to avoid an error. 
    assert(merge_lists_simple([3, 1], [2])) == [1, 2, 3]
    # the above is used to show how merge_lists_simple() will work even if 
    # either input list is unsorted 

    print("All tests passed!")

if __name__ == "__main__":
    test()

# merge_lists_best() review:
# Correctness:
#   - Works for all edge cases as long as both input lists are sorted ascending.
#   - If not, then output list will not be sorted
#
# Complexity:
#   - Time: O(len(list1) + len(list2))
#   - Space: O(len(list1) + len(list2)), mainly the output list 
#
# Readability:
#   - More complex than merge_sorted_simple(), but still readable and easy to understand
#
# Use case:
#   - For when both lists are already sorted and when priority is speed over readability

# merge_lists_simple() review:
# Correctness:
#   - Works for all edge cases with standard numerical lists, neither list has to be sorted
#
# Complexity:
#   - Time: O(N * log N), where N = len(list1) + len(list2).
#   - Space: O(len(list1) + len(list2)), solely for the output list
#
# Readability:
#   - Much simpler but slower than merge_lists_best()
#
# Use case:
#   - For when neither list has to be sorted and when priority is readability over speed