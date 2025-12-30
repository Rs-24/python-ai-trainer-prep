def rotate_string_long(string: str, rotation_index: int) -> str:
    if not string or rotation_index == 0:
        return string
    rotation_index = (rotation_index) % len(string) 
    result = [""] * len(string)
    for i in range(len(string)):
        index = (i + rotation_index) % len(string)
        result[index] = string[i]
    return "".join(result)

def rotate_string_simple(string: str, rotation_index: int) -> str:
    if not string or rotation_index == 0:
        return string
    rotation_index = (rotation_index) % len(string) 
    return string[-rotation_index:] + string[:-rotation_index]

def test():
    print("Running tests")    
    assert rotate_string_long("a", 5) == "a"
    assert rotate_string_simple("a", 5) == "a"

    assert rotate_string_long("abcdef", 6) == "abcdef"
    assert rotate_string_simple("abcdef", 6) == "abcdef"

    assert rotate_string_long("abcdef", 7) == "fabcde"
    assert rotate_string_simple("abcdef", 7) == "fabcde"

    assert rotate_string_long("abcd", 3) == "bcda"
    assert rotate_string_simple("abcd", 3) == "bcda"

    assert rotate_string_long("abcd", -1) == "bcda"
    assert rotate_string_simple("abcd", -1) == "bcda"

    assert rotate_string_long("abcd", 0) == "abcd"
    assert rotate_string_simple("abcd", 0) == "abcd"

    assert rotate_string_long("", 4) == ""
    assert rotate_string_simple("", 4) == ""
    print("All tests passed!")

if __name__ == "__main__":
    test()

# rotate_string_long() review:
# Correctness:
#   - Works for all edge cases
#   - Positive rotation index -> rotate right 
#   - Negative rotation index -> rotate left 
#
# Complexity:
#   - Time: O(len(string))
#   - Space: O(len(string)), mainly the result variable 
#
# Readability:
#   - More complex than rotate_string_simple(), but still readable and easy to understand
#
# Use case:
#   - For when teaching and helping people understand the algorithm is prioritised over readability

# rotate_string_simple() review:
# Correctness:
#   - Works for all edge cases
#   - Positive rotation index -> rotate right 
#   - Negative rotation index -> rotate left 
#
# Complexity:
#   - Time: O(len(string))
#   - Space: O(len(string)), mainly the returned string
# Readability:
#   - Much simpler than rotate_string_long()
#
# Use case:
#   - For when readability is prioritised over teaching/understanding of the algorithm