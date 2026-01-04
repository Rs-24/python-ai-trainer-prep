# Time to write all of below including tests, why the solution works and time 
# and space complexity: 9 mins

# Problem: https://leetcode.com/problems/sqrtx/description/

from typing import Callable

def sqrt(x: int) -> int:
    for i in range(0, x + 1):
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1

def run_tests(f: Callable[[int], int]) -> None:
    tests = [(25, 5), (24, 4), (1, 1), (0, 0), (2, 1)]
    for test, expected in tests:
        actual = f(test)
        assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(sqrt)
    print("All tests passed!")

if __name__ == "__main__":
    test()


# Why this solution works:
#   - A for loop is used to iterate i up to x inclusive, and if i*i = x then i 
#     is returned. If not, then if i*i > x then i-1 is returned
#
# Time complexity: O(x)
# Space complexity: O(1)
# 
# Learning lessons (done after completing all of above in 9 mins):
#   - In retrospect a binary method would have a better time complexity of
#     O(log x) while retaining O(1) auxiliary space complexity. Hence, I rewrote
#     the function, and the result is shown below: 
# 
# def sqrt(x: int) -> int:
#     left, right = 0, x
#     while left <= right:
#         mid = (left + right) // 2
#         sq = mid * mid
#         if sq < x:
#             left = mid + 1
#         elif sq > x:
#             right = mid - 1
#         else:
#             return mid
#     return right


