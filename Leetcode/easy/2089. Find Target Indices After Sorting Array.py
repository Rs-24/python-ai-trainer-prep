

class Solution:
    def targetIndices(self, nums: list, target: int) -> list:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        less = same = 0
        for num in nums:
            less += 1 if num < target else 0
            same += 1 if num == target else 0
        return [i for i in range(less, less + same)]


