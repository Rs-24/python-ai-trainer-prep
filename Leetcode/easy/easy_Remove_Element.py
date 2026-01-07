# Time to write all of below including tests, why the solution works and time 
# and space complexity: 57 mins

# Problem: https://leetcode.com/problems/remove-element/description/ 

from typing import List, Callable

def remove_element(nums: List[int], val: int) -> int:
    if not nums:
        return 0
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
    nums[left:] = [0] * (len(nums) - left)
    return left

def run_tests(f: Callable[[List[int], int], int]) -> None:
    tests = [([1, 2, 3, 3, 4], 3, [1, 2, 4, 0, 0], 3), ([], 2, [], 0), ([3, 3, 3], 3, [0, 0, 0], 0), ([1, 2, 3], 3, [1, 2, 0], 2)]
    for nums, val, expected_nums_after, expected_k in tests:
        before = nums.copy()
        actual_k = f(before, val)
        assert actual_k == expected_k, f"{f.__name__}({nums}, {val}) = {actual_k}, expected {expected_k}"
        assert before == expected_nums_after, f"{f.__name__}({nums}, {val}) changed {nums} to {before}, it should have been changed to {expected_nums_after}"

def test() -> None:
    print("Running tests...")
    run_tests(remove_element)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - if nums is empty, 0 is returned. Otherwise, a two pointer approach is
#     used while iterating over the list, and after the loop ends each instance
#     of val at the end is replaced with a zero
#
# Time complexity: O(len(nums))
# Auxiliary space complexity: len(nums)

# Learning lessons (done after completing all of above in 57 mins):
#   - The line 'nums[left:] = [0] * (len(nums) - left)' probably isn't
#     necessary, as the Leetcode problem page states it doesn't matter 
#     what is in the list after the first k elements where k is the number
#     of elements not equal to val.
#   - Currently with the line 'nums[left:] = [0] * (len(nums) - left)' I
#     stated auxiliary space complexity to be O(len(nums)), more specifically
#     it is O(len(nums) - k)
#   - Also, as mentioned I shouldn't have put in the 0's replacing each
#     instance of val so the tests should be altered by either replacing each 
#     instance of 0 with val, or just not check beyond the first k elements. In
#     this instance it would be better to not check beyond the first k elements
#     as the Leetcode problem page states anyway that it doesn't matter what is
#     in the list after the first k elements anyway. As such, run_tests() can
#     be changed into:
# 
# def run_tests(f: Callable[[List[int], int], int]) -> None:
#     tests = [([1, 2, 3, 3, 4], 3, [1, 2, 4], 3), ([], 2, [], 0), ([3, 3, 3], 3, [], 0), ([1, 2, 3], 3, [1, 2], 2)]
#     for nums, val, expected_first_k_elements, expected_k in tests:
#         before = nums.copy()
#         actual_k = f(before, val)
#         assert actual_k == expected_k, f"{f.__name__}({nums}, {val}) = {actual_k}, expected {expected_k}"
#         assert expected_first_k_elements == before[:actual_k], f"{f.__name__}({nums}, {val}) changes {nums} to {before}, but the first k elements should be {expected_first_k_elements}"




