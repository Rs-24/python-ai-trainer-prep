from typing import List, Callable

def has_subarray_with_sum_efficient(nums: List[int], target: int) -> bool:
    """
    Determines if there is a contiguous sequence of numbers within nums that
    sum to target, and returns True/False accordingly. Every element in nums
    must be >= 0 to ensure a correct output 
    """
    assert all(num >= 0 for num in nums), "Every element in nums must be >= 0"
    if not nums:
        return False
    left = 0
    window_sum = 0
    for right, num in enumerate(nums):
        window_sum += num
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        if window_sum == target and left <= right:
            return True
    return False

def has_subarray_with_sum_bruteforce(nums: List[int], target: int) -> bool:
    """
    Determines if there is a contiguous sequence of numbers within nums that
    sum to target, and returns True/False accordingly. There is no requirement
    for either target nor every element in nums to be >= 0 to ensure a correct
    output
    """
    if not nums:
        return False
    n = len(nums)
    for left in range(n):
        window_sum = 0
        for right in range(left, n):
            window_sum += nums[right]
            if window_sum == target:
                return True           
    return False

def run_test(function: Callable[[List[int], int], bool]):
    tests = [(([1, 2, 3], 2), True), (([2, 3, 4], 7), True), (([], 0), False), (([1, 2, 3], 6), True), (([1, 2, 3, 2], 5), True), (([5], 5), True), (([5], 3), False), (([1, 2, 0], 0), True), (([0, 0, 0], 0), True), (([0, 0, 0], 1), False), (([1, 2, 3], 100), False), (([1, 2, 3], 5), True), (([1, 2, 3], 8), False)]
    for test, expected in tests:
        actual = function(test[0], test[1])
        assert actual == expected, f"{function.__name__}({test}) == {actual}, expected {expected}"
    if function == has_subarray_with_sum_bruteforce:
        tests = (([1, -1, 2], 0), True), (([-1, -1, 5], 3), True), (([-1, -2, 4], -3), True), (([-1, -2, -4], -8), False)
        for test, expected in tests:
            actual = function(test[0], test[1])
            assert actual == expected, f"{function.__name__}({test}) == {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_test(has_subarray_with_sum_efficient)
    run_test(has_subarray_with_sum_bruteforce)
    print("All tests passed!")

if __name__ == "__main__":
    test()


# has_subarray_with_sum_efficient() review:
# Correctness:
#   - Works for all edge cases, however every element of nums must be >= 0 to ensure a correct output 
#   - Example edge cases: 
#      - returns False for an empty list, as no subarray exists
#      - all zeros, with target = 0, correctly returns True
#  
# Complexity:
#   - Time: O(n), where n = len(nums)
#   - Auxiliary space: O(1)
#
# Readability:
#   - Requires more lines of code and is slightly more difficult to understand how the algorithm works as to the sliding window logic is not as obvious as the brute force version at first glance
#
# Use case:
#   - For any production scenario due to its better time complexity
#
# has_subarray_with_sum_bruteforce() review:
# Correctness:
#   - Works for all edge cases. It is not a requirement for either target nor every element in nums to be >= 0 to ensure a correct output
#   - Example edge cases: 
#      - returns False for an empty list, as no subarray exists
#      - all zeros, with target = 0, correctly returns True
#      - works for all negative elements in nums, with a negative target
#
# Complexity:
#   - Time: O(n^2)
#   - Auxiliary space: O(1)
#
# Readability:
#   - Requires fewer lines of code and is more explicit, and hence it is easier to understand how the algorithm works
# Use case:
#   - For when trying to explain/understand how the algorithm works
#
# Final verdict:
#   - For production, I would advise using has_subarray_with_sum_efficient() due to its better time complexity of
#     O(n), meaning it will be much faster for larger sizes of nums assuming both target and every instance
#     in nums are >= 0
#   - For teaching, or understanding how the algorithm works, I would advise using has_subarray_with_sum_bruteforce()
#     as it is more explicit, requires fewer lines of code and does not use a sliding window logic which can be
#     difficult to understand at first. It does have a less efficient time complexity of O(n^2), however this
#     should not be an issue with small sizes of nums