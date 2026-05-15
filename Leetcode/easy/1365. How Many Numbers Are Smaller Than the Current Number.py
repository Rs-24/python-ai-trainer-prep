

class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        d = {num: i for i, num in enumerate(sorted(nums))}
        return [d[num] for num in nums]


