

class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        # Time: O(n^2), n = len(nums) = len(index)
        # Space: O(n)
        out = []
        for num, idx in zip(nums, index):
            out.insert(idx, num)
        return out


