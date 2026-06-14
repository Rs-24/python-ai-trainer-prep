

class Solution:
    def absDifference(self, nums: list, k: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        nums.sort(reverse=True)
        s = 0
        for i in range(k):
            s += nums[i]
        nums.reverse()
        for i in range(k):
            s -= nums[i]
        return s


