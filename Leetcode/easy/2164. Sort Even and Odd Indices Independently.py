

class Solution:
    def sortEvenOdd(self, nums: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        nums[1::2] = sorted(nums[1::2], reverse=True)
        nums[::2] = sorted(nums[::2])
        return nums


