# Time to write all of below including tests, why the solution works and time 
# and space complexity: 28 mins

# Problem: https://leetcode.com/problems/merge-sorted-array/description/

from typing import List, Callable

def merge(nums1: List[int], nums2: List[int], m: int, n: int) -> None:
    i, j = 0, 0
    new_nums: List[int] = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            new_nums.append(nums1[i])
            i += 1
        else:
            new_nums.append(nums2[j])
            j += 1
    new_nums.append(nums1[i:m])
    new_nums.append(nums2[j:])
    nums1 = new_nums

def run_tests(f: Callable[[List[int], List[int], int, int], None]):
    tests = [([-5, -1, 3, 0, 0, 0], [2, 4, 6], 3, 3, [-5, -1, 2, 3, 4, 6]), ([0, 2], [], 2, 0, [0, 2]), ([0], [1], 0, 1, [1]), ([0], [1], 0, 1, [1])]
    for nums1, nums2, m, n, expected in tests:
        before = nums1.copy()
        f(nums1, nums2, m, n)
        assert nums1 == before, f"{f.__name__}({nums1}, {nums2}, {m}, {n}) changes {before} to {nums1}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(merge)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - The function iterates across nums1 and nums2 while building a new sorted list
#     new_nums. Once the loop ends any remaining numbers are appended (except from
#     any zeros in nums1 after the first m numbers), and nums1 is set to new_nums
#
# Time complexity: O(m + n)
# Space complexity: O(m + n)
#
# Learning lessons (done after completing all of above in 28 mins):
#   - After debugging errors, I found that 'nums1 = new_nums' doesn't actually
#     change nums1 outside the function, hence it should be 'nums1[:] = new_nums'
#   - The lines 'new_nums.append(nums1[i:m])' and 'new_nums.append(nums2[j:])' 
#     append the substrings as lists instead of appending the individual elements,
#     hence I should have used .extend() instead of .append()
#   - 'nums1 == before' should actually be 'nums1 == expected'
#   - There is actually a better method with O(1) auxiliary space complexity and
#     O(m + n) time complexity, and hence I rewrote my code, with my new O(1)
#     auxiliary space and O(m + n) time code below:
#
# def merge(nums1: List[int], nums2: List[int], m: int, n: int) -> None:
#     i, j = m - 1, n - 1
#     insert_pos = m + n - 1
#     while i >= 0 and j >= 0 and insert_pos >= 0:
#         if nums1[i] < nums2[j]:
#             nums1[insert_pos] = nums2[j]
#             insert_pos -= 1
#             j -= 1
#         else:
#             nums1[insert_pos] = nums1[i]
#             insert_pos -= 1
#             i -= 1
#     while j >= 0:
#         nums1[insert_pos] = nums2[j]
#         insert_pos -= 1
#         j -= 1

