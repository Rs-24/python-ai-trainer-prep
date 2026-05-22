

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        if len(password) < 8 or not any(ch.islower() for ch in password) or not any(ch.isupper() for ch in password) or not any(ch.isdigit() for ch in password) or not any(ch in "!@#$%^&*()-+" for ch in password):
            return False
        prev = None
        for ch in password:
            if ch == prev:
                return False
            prev = ch
        return True


