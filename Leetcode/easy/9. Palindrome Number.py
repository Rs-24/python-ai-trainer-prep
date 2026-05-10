

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Time: O(log x)
        # Space: O(1)
        if x < 0:
            return False
        if x <= 9:
            return True
        if x % 10 == 0:
            return False
        rev = 0
        original = x
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == original


