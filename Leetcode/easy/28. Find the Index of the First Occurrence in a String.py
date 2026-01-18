# Time to write all of below including tests, why the solution works and time 
# and space complexity: 15 mins

# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

from typing import Callable

def first_occurrence(needle: str, haystack: str) -> int:
    length = len(needle)
    for i in range(0, len(haystack) - len(needle)):
        if haystack[i:i+length] == needle:
            return i
    return -1

def run_tests(f: Callable[[str, str], int]) -> None:
    tests = [("needle", "haystack", -1), ("hi", "hiya", 0), ("ship", "worship", 3), ("wheelbarrow", "bar", 5)]
    for needle, haystack, expected in tests:
        actual = f(needle, haystack)
        assert actual == expected, f"{f.__name__}({needle}, {haystack}) = {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_tests(first_occurrence)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - haystack is iterated over and each substring is compared to needle and
#     the index at which the first instance of needle starts is returned. If
#     the loop ends and the code after it runs, then needle is not in haystack
#     and -1 is returned
#
# Time complexity: O(len(needle) * len(haystack))
# Auxiliary space complexity: O(len(needle))
# 
# Learning lessons (done after completing all of above in 15 mins):
#   - The line 'for i in range(0, len(haystack) - len(needle)):' should actually
#     be 'for i in range(0, len(haystack) - len(needle) + 1):'




