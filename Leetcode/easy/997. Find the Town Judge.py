

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Time: O(m + n), m = len(trust)
        # Space: O(n)
        score = [0] * n
        for a, b in trust:
            score[a - 1] -= 1
            score[b - 1] += 1
        for i, s in enumerate(score):
            if s == n - 1:
                return i + 1
        return -1


