from typing import Callable

def longest_unique_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.
    Uses a sliding window with a set.
    """
    seen = set()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        window_len = right - left + 1
        if window_len > best:
            best = window_len
    return best

# Note: the above code was obtained via chatGPT, the below tests were created by me

def run_test(f: Callable[[str], int]) -> None:
    tests = [("", 0), ("dvdf", 3), ("6b{]_%", 6), ("1212", 2), ("aBcD", 4), ("abba", 2), ("bbbb", 1), ("pwwkew", 3), ("tmmzuxt", 5)]
    for test, expected in tests:
        actual = f(test)
        assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_test(longest_unique_substring)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Review: longest_unique_substring(s: str):
#
# Summary: 
#   - The function uses a sliding window and the set 'seen', and iterates 
#     through the string to find the longest substring without repeating
#     characters
#
# How the code works:
#   - The code uses a set called seen to store all characters in the current
#     window to determine whether the current character is a duplicate or not
#   - The sliding window is defined by [left, right], and a for loop is used
#     to iterate over the string
#   - If the current character (at index 'right'), is in the seen set, the
#     window is shortened by incrementing left and removing the character 
#     that corresponds to the left index in s, until there are no duplicates 
#     in the window
#   - During each iteration after adjusting the window the current character
#     is added to the set, and the window length is compared to best, ensuring
#     it holds the longest length when the loop ends
#   - Once the loop ends, the function returns best
#
# Complexity:
#   - Time: O(n), where n = len(s)
#   - Space: O(n) in worst case if all characters in s are unique
#
# Readability:
#   - The function flow is very explicit and easy to understand, especially 
#     with the set 'seen'
#   - The variable names are clear and concise
#   - The docstring correctly states what the function does and returns
#
# Correctness:
#   - The function correctly implements the sliding window logic
#   - It handles duplicates well via the seen set and the adjusting of the window
#     window_len
#   - It correctly compares the current window length to best every iteration
#   - Once the for loop ends, it correctly returns best, and if the string is
#     empty, it returns 0, which is reasonable
#   - Hence, I would class this as a suitably correct solution 
#
# Tests:
#   - Current tests include empty string, special characters, 
#     multiple unique substrings of same length, and lower and uppercase 
#     letters, and the function passed them all
#   - Further tests could include e.g. very long inputs to test the time
#     complexity
#
# Improvements:
#   - The docstring already states it returns the length, however could also
#     explicitly state that it doesn't return the substring itself, and also
#     note that the function is case-sensitive and no characters are filtered
#     out, e.g. special characters
#   - The function could also be altered to also return the substring itself
#     alongside its length, and if so include failsafe logic for if there 
#     are two longest substrings (e.g. outputting the one that appears first),
#     and this should be mentioned in the docstring as well. Even if this is
#     not required in the problem statement, it can be useful if required in
#     future
#  
# Use case:
#   - The program is very easy to understand and has an optimal time complexity
#     and linear space complexity, making this suitable for production as long
#     as the substring itself is not required.
#   - If in future the longest substring itself is required, then the function
#     and tests will need to be adjusted accordingly 
#
# Score:
#   - Complexity/efficiency: 5/5
#   - Readability: 4/5
#   - Correctness: 5/5
#   - Testing: 4/5
#   - Overall: accept with minor docstring improvements
#
# Verdict:
#   - Efficent and correct solution. I would accept this, potentially with
#     minor docstring clarifications 






