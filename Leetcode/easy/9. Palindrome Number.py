# Time to write all of below including tests, explanation and time and aux 
# space: 6 mins

# Problem: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x >= 0 and x <= 9:
            return True
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(-1) == False
    assert sol.isPalindrome(0) == True
    assert sol.isPalindrome(5) == True
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindrome(121) == True

# Explanation: x is converted to an int, and checked against its reversed
# equivalent.
# Time: O(n), n = number of digits in x
# Aux space: O(n)

# Learning lessons (done after completing all of above in 6 mins):
#   - There is a typo: my explanation says: "x is converted to an int",
#     actually it should say: "x is converted to a string"
#   - It would be useful to know the method which doesn't involve converting
#     to a string. My attempt is below:
#
# def isPalindrome(self, x: int) -> bool:
#     # Time: O(n), n = number of digits in x
#     # Aux space: O(1)
#     if x < 0 or (x != 0 and x % 10 == 0):
#         return False
#     reversed_half = 0
#     while x > reversed_half:
#         reversed_half = reversed_half * 10 + (x % 10)
#         x //= 10
#     return x == reversed_half or x == reversed_half // 10


def isPalindrome(self, x: int) -> bool:
    original = x
    rev = 0

    while x > 0:
        rev = (rev * 10) + (x % 10)
        x //= 10
    
    return rev == original




