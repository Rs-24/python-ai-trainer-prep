from typing import List, Dict

def check_anagram_long(s1: str, s2: str) -> bool:
    str1: List[str] = []
    str2: List[str] = []
    for ch in s1.lower():
        if ch != " ":
            str1.append(ch) 
    for ch in s2.lower():
        if ch != " ":
            str2.append(ch)
    if len(str1) != len(str2):
        return False
    for ch in str1:
        if ch in str2:
            str2.remove(ch)
        else:
            return False
    return True

def get_dict_simple(s: str) -> Dict[str, int]:
    s_dict: Dict[str, int] = {}
    for ch in s.lower():
        if ch == " ":
            continue
        if ch not in s_dict:
            s_dict[ch] = 1
        else:
            s_dict[ch] += 1
    return s_dict

def check_anagram_simple(s1: str, s2: str) -> bool:
    return get_dict_simple(s1) == get_dict_simple(s2)

def test():
    print("Running tests...")

    assert check_anagram_long("listen", "silent") == True
    assert check_anagram_simple("listen", "silent") == True

    assert check_anagram_long("a b aa", "aaa b") == True
    assert check_anagram_simple("a b aa", "aaa b") == True

    assert check_anagram_long("Hello", "World") == False
    assert check_anagram_simple("Hello", "World") == False

    assert check_anagram_long("A t om", "m O aTs") == False
    assert check_anagram_simple("A t om", "m O aTs") == False

    assert check_anagram_long("", "") == True
    assert check_anagram_simple("", "") == True

    assert check_anagram_long("a", "") == False
    assert check_anagram_simple("a", "") == False

    assert check_anagram_long("A", "a") == True
    assert check_anagram_simple("A", "a") == True

    assert check_anagram_long("aab", "abb") == False
    assert check_anagram_simple("aab", "abb") == False

    print("All tests passed!")

if __name__ == "__main__":
    test()

# check_anagram_long() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(n^2) at its worst case, where n is the length of either list as
#     both lists must be equal in length for comparisons to occur
#   - Space: O(n + m)
#
# Readability:
#   - More complex than check_anagram_simple(), but easier to understand how the algorithm works
#
# Use case:
#   - For when teaching and helping people understand the algorithm is prioritised over readability

# check_anagram_simple() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(n + m), where n and m are the lengths of each input string, respectively
#   - Space: O(n + m)
#
# Readability:
#   - More concise than check_anagram_long()
#
# Use case:
#   - For when readability is prioritised over teaching/understanding of the algorithm



