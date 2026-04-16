# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/description/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(n)
        prev = None
        for part in s.split():
            if part.isdigit():
                if prev is not None and prev >= int(part):
                    return False
                prev = int(part)
        return True


