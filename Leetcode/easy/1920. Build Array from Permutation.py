

class Solution:
    def buildArray(self, nums: list) -> list:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        out = []
        for i in range(len(nums)):
            out.append(nums[nums[i]])
        return out


