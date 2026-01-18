# Time to write all of below including tests, why the solution works and time 
# and space complexity: 10 mins

# Problem: https://leetcode.com/problems/length-of-last-word/description/

from typing import Callable

def last_word_length(s: str) -> int:
    if not s:
        return 0
    return len(s.strip().split()[-1])

def run_test(f: Callable[[str], int]) -> None:
    tests = [("Hi there", 5), ("Good bye", 3), ("Hi", 2), ("The moon    isfar3  ", 6)]
    for s, expected in tests:
        actual = f(s)
        assert actual == expected, f"{f.__name__}({s!r}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_test(last_word_length)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - If s is empty, 0 is returned. Otherwise, all leading and trailing
#     whitespace is stripped from s, and it is split into it's separate
#     words. Then the length of the last word is returned
#
# Time complexity: O(len(s))
# Auxiliary space complexity: O(1)
#
# Learning lessons (done after completing all of above in 10 mins):
#   - Auxiliary space complexity is actually O(len(s)) due to .split()
#   - Upon further thought, I have found there is a way of doing it with O(1)
#     auxiliary space complexity:  
#
# def last_word_length(s: str) -> int:
#     length = 0
#     i = len(s) - 1
#     while i >= 0:
#         if s[i] != " ":
#             length += 1
#         elif length > 0:
#             return length
#         i -= 1
#     return length

    
