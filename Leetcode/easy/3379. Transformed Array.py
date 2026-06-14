

class Solution:
    def constructTransformedArray(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        for i, num in enumerate(nums):
            out.append(nums[(i + num) % len(nums)])
        return out


