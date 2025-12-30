from typing import Dict, Callable

def first_unique_char_bruteforce(s: str) -> int:
    for i, ch in enumerate(s):
        if ch not in (s[:i] + s[i + 1:]):
            return i
    return -1

def first_unique_char_hashmap(s: str) -> int:
    chars: Dict[str, int] = {}
    for ch in s:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    for i, ch in enumerate(s):
        if chars[ch] == 1:
            return i
    return -1

def run_test(function_name: Callable[[str], int]):
    tests = [("abcbc", 0), ("aA", 0), ("aabbcdde", 4), ("", -1), ("a!2", 0), ("11aa66o2e3", 6), ("a", 0), ("aabb", -1), ("aabbc", 4), ("abc", 0)]
    for test, expected in tests:
        actual = function_name(test)
        assert actual == expected, f"{function_name.__name__}({test!r}): actual: {actual}, expected: {expected}"

def test():
    print("Running tests...")
    run_test(first_unique_char_bruteforce)
    run_test(first_unique_char_hashmap)
    print("All tests passed!")

if __name__ == "__main__":
    test()
    
# first_unique_char_bruteforce() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(len(s)^2)
#   - Space: O(len(s))
#
# Readability:
#   - More concise than first_unique_char_hashmap(), however not as easy to understand how algorithm works as it is hidden behind the slicing, and also it is less efficient with a O(len(s)^2) time complexity
#
# Use case:
#   - For when readability is prioritised over teaching and understanding the algorithm

# first_unique_char_hashmap() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(len(s))
#   - Space: O(len(s))
#
# Readability:
#   - More explicit and hence redundant than first_unique_char_bruteforce(), however easier to understand how the algorithm works and more efficient with a O(len(s)) time complexity
#
# Use case:
#   - For when teaching and understanding the algorithm is prioritised over readability
#
# Verdict:
#   - first_unique_char_bruteforce() has an O(len(s)^2) behaviour, so will take
#     significantly longer while first_unique_char_hashmap() is linear and would 
#     take comparatively less time
#   - I would advise using first_unique_char_hashmap() for production and
#     first_unique_char_bruteforce() as a teaching example
