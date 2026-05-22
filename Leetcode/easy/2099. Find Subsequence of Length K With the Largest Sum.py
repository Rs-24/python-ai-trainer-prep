

class Solution:
    def maxSubsequence(self, nums: list, k: int) -> list:
        # Time: O(n log n), n = len(nums)
        # Space: O(n)
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x[0], reverse=True)
        nums = nums[:k]
        nums.sort(key=lambda x: x[1])
        return [num for num, _ in nums]


