

class Solution:
    def findKDistantIndices(self, nums: list, key: int, k: int) -> list:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        s = set()
        a = [i for i, num in enumerate(nums) if num == key]
        for i in a:
            for di in range(-k, k + 1):
                if 0 <= i + di < len(nums):
                    s.add(i + di)
        return sorted(list(s))


