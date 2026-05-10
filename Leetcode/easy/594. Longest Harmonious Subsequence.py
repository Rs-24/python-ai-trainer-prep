

from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        c = Counter(nums)
        best = 0
        for num, freq in c.items():
            if num + 1 in c:
                best = max(best, freq + c[num + 1])
        return best


