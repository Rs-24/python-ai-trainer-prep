

class Solution:
    def minOperations(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set()
        for n in nums:
            if n < k:
                return -1
            if n > k:
                s.add(n)
        return len(s)


