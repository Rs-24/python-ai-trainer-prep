# Time to write all of below including tests, why the solution works and time 
# and space complexity: 22 mins

# Problem: https://leetcode.com/problems/search-insert-position/description/

from typing import List, Callable

def insert_position(nums: List[int], target: int) -> int:
    if not nums:
        return 0
    left, right = 0, len(nums) - 1
    while left <= right:
        if left == right:
            if nums[left] < target:
                    return left + 1
            elif nums[left] > target:
                if left == 0:
                    return left
                else:
                    return left - 1
            else:
                return left
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
def run_tests(f: Callable[[List[int], int], int]) -> None:
    tests = [([1, 2, 3], 2, 1), ([1, 2, 3], 4, 3), ([1, 2, 3], 0, 0)]
    for nums, target, expected in tests:
        actual = f(nums, target)
        assert actual == expected, f"{f.__name__}({nums}, {target}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(insert_position)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - If nums is empty, then zero is returned. Otherwise, a binary search is used
#     to find the value. If found, the corresponding index is returned and if not
#     found, the index where it should be is returned
# 
# Time complexity: O(log(len(nums)))
# Auxiliary space complexity: O(1)
#
#
# Learning lessons (done after completing all of above in 22 mins):
#   - The code block:
#     'if left == 0:
#         return left
#     else:
#         return left - 1'
#     should actually just be:
#     'return left'
#   - A final return would have been a good failsafe, and the correct return 
#     would be 'return left'
#   - Additionally, the code could be simplified to the below:
# 
# def insert_position(nums: List[int], target: int) -> int:
#     if not nums:
#         return 0
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left


