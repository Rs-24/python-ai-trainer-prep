def palindrome_checker_long(s: str) -> bool:
    backwards = []
    for i in range(len(s) - 1, -1, -1):
        backwards.append(s[i])
    backwards = "".join(backwards)
    return s == backwards

def reverse_string_best(s: str) -> str:
    return s[::-1]

def palindrome_checker_best(s: str) -> bool:
    return s == reverse_string_best(s)

def test():
    print("Running tests...")

    assert palindrome_checker_long("") == True
    assert palindrome_checker_best("") == True

    assert palindrome_checker_long("1") == True
    assert palindrome_checker_best("1") == True

    assert palindrome_checker_long("a") == True
    assert palindrome_checker_best("a") == True

    assert palindrome_checker_long("Racecar") == False
    assert palindrome_checker_best("Racecar") == False

    assert palindrome_checker_long("racecar") == True
    assert palindrome_checker_best("racecar") == True

    assert palindrome_checker_long("123") == False
    assert palindrome_checker_best("123") == False

    assert palindrome_checker_long("123321") == True
    assert palindrome_checker_best("123321") == True

    print("All tests passed!")

if __name__ == "__main__":
    test()

# palindrome_checker_long() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(N), where N = len(s)
#   - Space: O(N), where N = len(s), mainly from backwards variable
#
# Readability:
#   - More complex than palindrome_checker_best(), but easier to understand how the algorithm works
#
# Use case:
#   - For when teaching and helping people understand the algorithm is prioritised over readability

# palindrome_checker_best() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(N), where N = len(s)
#   - Space: O(N), where N = len(s)
#
# Readability:
#   - More concise than palindrome_checker_long()
#
# Use case:
#   - For when readability is prioritised over teaching/understanding of the algorithm