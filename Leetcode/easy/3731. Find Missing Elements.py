

class Solution:
    def findMissingElements(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        return [x for x in range(min(nums), max(nums) + 1) if x not in s]


