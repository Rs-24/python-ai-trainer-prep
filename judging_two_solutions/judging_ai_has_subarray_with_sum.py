from typing import List, Callable

def has_subarray_with_sum_candidate(nums: List[int], target: int) -> bool:
    """
    Returns True if there exists a contiguous subarray in nums whose sum equals target.

    This implementation is intended to work with both positive and negative integers.
    Time complexity: O(n), Space complexity: O(1).
    """
    left = 0
    current_sum = 0

    for right, value in enumerate(nums):
        current_sum += value

        # Shrink the window while the sum is greater than target
        while current_sum > target and left < right:
            current_sum -= nums[left]
            left += 1

        if current_sum == target:
            return True

    return False

# Note: the above code was obtained via chatGPT, the below tests were written by me

def run_test(f: Callable[[List[int], int], bool]):
    tests = [([1, 2, 3], 5, True), ([1, 2, 3], 1, True), ([], 0, False), ([], 5, False), ([1, 2, 3], 7, False)]
    for nums, target, expected in tests:
        actual = f(nums, target)
        assert actual == expected, f"{f.__name__}({nums}, {target}) = {actual}, expected {expected}"

def run_test_bugs(f: Callable[[List[int], int], bool]):
    """
    These are tests involving negative numbers which return False, but
    should instead return True, meaning the commented assert would fail. This 
    is to illustrate how the function does not work with negative numbers
    """
    tests = [([-3, -2], -2, True), ([-7, -6, -5], -6, True)]
    for nums, target, expected in tests:
        actual = f(nums, target)
        assert actual == expected, f"{f.__name__}({nums}, {target}) = {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_test(has_subarray_with_sum_candidate)
    run_test_bugs(has_subarray_with_sum_candidate)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Review: has_subarray_with_sum_candidate()
#
# Summary:
#   - The code iterates through nums using a sliding window approach to
#     find a contiguous subarray that sums to target. If so, it returns
#     True and if not returns False. There is a major issue with the sliding 
#     window however in that it cannot handle negative numbers despite saying
#     this in the docstring, which is further explained below  
#
# How the code works:
#   - The sliding window is defined by [left, right], and during each iteration,
#     current_sum is compared to target and the sliding window is adjusted
#     accordingly, albeit incorrectly as it cannot handle negative numbers (more
#     below). If current sum is equal to target, the function returns
#     True, and if the loop ends without finding a contiguous subarray, it 
#     returns False 
#
# Complexity:
#   - Time: O(n), where n = len(nums)
#   - Auxiliary space: O(1)
#   - Note: this complexity is optimal however the function does not produce
#           a correct result with negative integers, and in this scenario an
#           optimal complexity would be meaningless 
#
# Readability:
#   - All the variables are appropriately named and easy to understand
#   - The program flow is very explicit and easy to understand despite the flaw
#     of not being able to handle negative numbers 
#   - Although the docstring is not fully correct as explained below, it still
#     clearly states what the program does and returns as explained below
#
# Correctness:
#   - The program uses a sliding window approach by iterating though nums. The 
#     general idea is correct however the implementation is partially wrong
#   - current_sum is incremented by the current value in nums per iteration, as
#     expected
#   - Per iteration the sliding window is adjusted if necessary (albeit 
#     incorrectly as explained below) and if current_sum is equal to target, then
#     the function returns True, which is the expected behaviour
#   - If the for loop ends then a contiguous subarray hasn't been found, in
#     which case return False ensures the correct output
#   - However, the docstring states that it works with both positive and
#     negative integers which is not true due to the 
#     "while current_sum > target..." line. Because e.g. -3 is not > -2 and as
#     such the window would not be shrunk. Meaning if the next number is -2,
#     current_sum becomes -5 and not -2, meaning the -2 is lost even though 
#     it is equal to target. Hence the line only works with non-negative numbers
#   - Hence the function is only partially correct, as for negative numbers the
#     sliding window may produce an incorrect result
# 
# Tests:
#   - Tests include standard inputs as well as edge cases such as nums being 
#     empty, negative targets and all negative elements in nums 
#   - Further tests could include e.g. nums being very large to test the
#     time complexity
#   - There are also tests to prove that the function can't handle negative
#     numbers, which are in run_test_bugs()
#
# Improvements:
#   - As mentioned, the docstring states that it works for both positive and
#     negative integers which is not true. As such the function does not meet
#     the problem specification, and hence the code should be altered to meet
#     the requirements
#   - The docstring does state that the function returns True if a contiguous
#     subarray is found, however the function also returns False if it is not
#     found, and the docstring could state this as well
#
# Score:
#   - Complexity: 5/5
#   - Readability: 5/5
#   - Correctness: 3/5
#   - Tests: 4/5
#   - Overall: Only accept if code is adjusted to handle negative numbers
#
# Verdict:
#   - Optimally efficient and easy to understand solution, however cannot 
#     handle negative numbers which is stated in the problem specification.
#     Hence the code must be adjusted to handle negative numbers before it 
#     can be accepted