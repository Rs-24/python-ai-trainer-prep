

class Solution:
    def numberOfPoints(self, nums: list[list]) -> int:
        # Time: O(1)
        # Space: O(1)
        s = set()
        for a, b in nums:
            for i in range(a, b + 1):
                s.add(i)
        return len(s)


