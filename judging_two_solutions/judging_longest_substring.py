from typing import Dict, Set, Callable, Tuple

def longest_substring_efficient(s: str) -> Tuple[int, str]:
    """
    Finds longest substring with no duplicate characters, returns the length
    of the string, and the string itself. If there are multiple of these
    strings, it returns the one that appears first
    """
    if not s:
        return 0, ""
    max_left = 0
    max_len = 0
    left = 0
    seen: Dict[str, int] = {}
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        length = right - left + 1
        if length > max_len:
            max_left = left
            max_len = length
    return max_len, s[max_left:max_left+max_len]

def longest_substring_bruteforce(s: str) -> Tuple[int, str]:
    """
    Finds longest substring with no duplicate characters, returns the length
    of the string, and the string itself. If there are multiple of these
    strings, it returns the one that appears first
    """
    if not s:
        return 0, ""
    max_left = 0
    max_right = 0
    for i in range(len(s)):
        seen: Set[str] = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            else:
                seen.add(s[j])
            if j - i > max_right - max_left:
                max_left = i
                max_right = j
    return max_right - max_left + 1, s[max_left:max_right+1]

def run_test(function: Callable[[str], Tuple[int, str]]):
    tests = [("", (0, "")), ("a", (1, "a")), ("abba", (2, "ab")), ("bbbb", (1, "b")), ("pwwkew", (3, "wke")), ("tmmzuxt", (5, "mzuxt")), ("abc", (3, "abc")), ("dvdf", (3, "vdf")), ("abca", (3, "abc")), ("aabcd", (4, "abcd"))]
    for test, expected in tests:
        actual = function(test)
        # assert actual == expected, f"{function.__name__}({test!r}) == {actual}, expected {expected}"
        # Above is to check if the specific substring is correct. It is not necessary, however it can
        # be commented out if desired
        assert actual[0] == len(actual[1]), f"{function.__name__}({test!r}) == {actual}, however the length of {actual[1]} != {actual[0]}"
        assert actual[0] == expected[0], f"{function.__name__}({test!r}) == {actual}, which is not same length as {expected}"
        assert len(set(actual[1])) == len(actual[1]), f"{function.__name__}({test!r}) == {actual}, which contains non-unique characters"

def test():
    print("Running tests...")
    run_test(longest_substring_efficient)
    run_test(longest_substring_bruteforce)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# longest_substring_efficient() review:
# Correctness:
#   - works for all edge cases, e.g. empty string, single characters, repeating characters, multiple longest substrings with no repeating characters
#
# Complexity:
#   - Time: O(len(s))
#   - Space: O(len(s)), mainly due to the seen dictionary
#
# Readability:
#   - Requires the same amount of code, but is slightly more difficult to understand how the algorithm works as it hidden behind the seen dictionary, however it does have a better time complexity
#
# Use case:
#   - For any production scenario, as it is more efficient than longest_substring_bruteforce()

# longest_substring_bruteforce() review:
# Correctness:
#   - works for all edge cases, e.g. empty string, single characters, repeating characters, multiple longest substrings with no repeating characters
#
# Complexity:
#   - Time: O(len(s)^2)
#   - Space: O(len(s)), mainly from the set 'seen'
#
# Readability:
#   - Easier to understand how the algorithm works as it is more explicit, however it is not as efficient
#
# Use case:
#   - For teaching purposes, but not for production
#
# Verdict:
#   - Due to its O(len(s)^2) time complexity, longest_substring_bruteforce()
#     will take significantly longer, and hence I would advise 
#     longest_substring_efficient() for production instead as it has a O(len(s))
#     time complexity.
#   - However, despite its worse time complexity, it is easier to understand how
#     the algorithm works with longest_substring_bruteforce(), and hence I would 
#     advise using it for teaching purposes