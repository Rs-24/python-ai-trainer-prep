# Time to write all of below including tests, why the solution works and time 
# and space complexity: 25 minutes

# Problem: https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02

from typing import List, Dict, Callable

def n_repeated_element(nums: List[int]):
    assert len(nums) >= 2 and len(nums) <= 5000, "len(nums) must be >= 2 and <= 5000"
    assert all(num >= 0 and num <= 10**4 for num in nums), "All values in nums must be >= 0 and <= 10^4"
    n = len(nums)/2
    freqs: Dict[int, int] = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
        if freqs[num] == n:
            return num
    return None

def run_test(f: Callable[[List[int]], int]) -> None:
    tests: List[any] = [([1, 2, 3, 3], 3)]
    for test, expected in tests:
        actual = f(test)
        assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_test(n_repeated_element)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why the solution works:
#   - asserts are used to ensure 2 <= len(nums) <= 5000, and that every element
#     in nums is >= 0 and <= 10**4
#   - Additionally, a dictionary is used to find the frequency of each element
#     in nums and if the frequency of the current element is n, then that element
#     is returned
# Time complexity: O(len(nums))
# Space complexity: O(len(nums))



# Learning lessons (done after completing all of above in 25 minutes):
#   - n = len(nums)/2 should be an int not a float even though in this instance
#     it works as 2.0 = 2, but still n = len(nums)//2 would be better
#   - Technically return None isn't needed as the problem specification states
#     states that nums will always contain an element repeated n times, then
#     the type hint -> int can be used
#   - A better way would be to return the first element that repeats which would
#     also produce the same result
#   - List[any] should be List[Any], and Any should be imported from Typing
#   - Asserts in def n_repeated_element probably isn't necessay as the
#     Leetcode constraints are guaranteed anyway








