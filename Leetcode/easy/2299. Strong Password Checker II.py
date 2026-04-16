# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/strong-password-checker-ii/description/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # Time: O(n), n = len(password)
        # Space: O(1)
        if len(password) < 8 or not any(ch.isupper() for ch in password) or not any(ch.islower() for ch in password) or not any(ch.isdigit() for ch in password) or not any(ch in "!@#$%^&*()-+" for ch in password):
            return False
        prev = None
        for ch in password:
            if ch == prev:
                return False
            prev = ch
        return True


