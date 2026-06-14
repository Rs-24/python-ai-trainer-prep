

class Solution:
    def smallestAbsent(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        a = max(1, int(sum(nums) / len(nums)) + 1)
        while a in s:
            a += 1
        return a


