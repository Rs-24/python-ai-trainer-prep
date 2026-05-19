

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        cur0 = best0 = cur1 = best1 = 0
        for ch in s:
            if ch == "0":
                cur0 += 1
                cur1 = 0
            else:
                cur0 = 0
                cur1 += 1
            best0 = max(best0, cur0)
            best1 = max(best1, cur1)
        return best1 > best0


