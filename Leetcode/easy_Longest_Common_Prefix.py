# Time to write all of below including tests, why the solution works and time 
# and space complexity: 16 minutes

# Problem: https://leetcode.com/problems/longest-common-prefix/description/ 

from typing import List, Callable

def longest_common_prefix(strings: List[str]) -> str:
    current = ""
    for ch in strings[0]:
        if all((current + ch) == s[:len(current)+1] for s in strings):
            current += ch
        else:
            return current
    return current

def run_test(f: Callable[[List[str]], str]) -> None:
    tests = [(["hi", "hello", "hiya"], "h"), (["", ""], ""), (["hi", "bye"], ""), (["lorry", "lore", "love"], "lo")]
    for test, expected in tests:
        actual = f(test)
        assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_test(longest_common_prefix)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this method works:
#   - current is set to "", after that ch is iterated through the first string
#     if current + ch is in the beginning of all the strings, and if not, then
#     current is returned.
# 
# Time complexity: O(n^2), where n is length of the shortest string in strings
# Space complexity: O(n)


# Learning lessons (done after completing all of above in 16 minutes):
#   - For robustness, I could have added in:
#     if not strings:
#         return "" 
#   - Time complexity is more specifically O(m * (n^2)) where n is the length 
#     of the shortest string, and m is number of strings in strings
#   - Also, an O(m * n) time complexity could have been possible via avoiding
#     string concatenation. The below is my rewrite after having now realised
#     that fact:
# 
# def longest_common_prefix(strings: List[str]) -> str:
#     if not strings:
#         return ""
#     right = 0
#     for ch in strings[0]:
#         if not all(len(s) >= (right + 1) and ch == s[right] for s in strings):
#             return strings[0][:right]
#         right += 1
#     return strings[0]


        

