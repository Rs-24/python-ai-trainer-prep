# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/find-the-town-judge/description/

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time: O(m + n), m = len(trust)
        # Space: O(n)
        score = [0] * n
        for a, b in trust:
            score[b - 1] += 1
            score[a - 1] -= 1
        for i, s in enumerate(score):
            if s == n - 1:
                return i + 1
        return -1


