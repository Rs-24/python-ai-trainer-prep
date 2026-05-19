

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1) 
        count = 0
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                count += 1
        return count


