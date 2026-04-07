# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Time: O(n), n = len(text)
        # Space: O(1)
        count = [0] * 26
        for ch in text:
            count[ord(ch) - ord("a")] += 1
        count[11] //= 2
        count[14] //= 2
        return min(count[i] for i in [1, 0, 11, 14, 13])


