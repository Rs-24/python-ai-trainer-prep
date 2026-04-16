# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        best_1 = cur_1 = best_0 = cur_0 = 0
        for ch in s:
            if ch == "1":
                cur_0 = 0
                cur_1 += 1
            else:
                cur_1 = 0
                cur_0 += 1
            best_1 = max(best_1, cur_1)
            best_0 = max(best_0, cur_0)
        return best_1 > best_0


