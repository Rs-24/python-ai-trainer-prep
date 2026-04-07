# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

class Solution:
    def maxScore(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        ones = s.count("1")
        zeros = 0
        best = 0
        for ch in s[:-1]:
            if ch == "0":
                zeros += 1
            else:
                ones -= 1
            best = max(best, zeros + ones)
        return best


