# Time to write all of below including tests, why the solution works and time 
# and space complexity: 2h 22 mins

# I couldn't figure this one out for some reason, and I required help from
# chatGPT to solve it

# Problem: https://leetcode.com/problems/climbing-stairs/description/

from typing import Callable 

def climbing_stairs(n: int) -> int:
    if n <= 3:
        return n
    prev = 3
    prev_prev = 2
    total = 0
    for i in range(4, n + 1):
        total = prev + prev_prev
        prev_prev = prev
        prev = total
    return total

def run_tests(f: Callable[[int], int]) -> None:
    tests = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8)]
    for test, expected in tests:
        actual = f(test)
        assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(climbing_stairs)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - If n <= 3, then 3 is returned. Otherwise, the function iterates from 4 to
#     n and the number of the ways for the previous and previous previous values
#     of n are summed for the current value of n and the final total is returned
#
# Time complexity: O(n)
# Space complexity: O(1)
# 
# Learning lessons (done after completing all of above in 2h 22 mins):
#   - I noticed a typo in my explanation: the line "If n <= 3, then 3 is returned"
#     should be changed to "If n <= 3, then n is returned"






