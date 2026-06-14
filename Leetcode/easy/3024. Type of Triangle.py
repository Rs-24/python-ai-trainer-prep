

class Solution:
    def triangleType(self, nums: list) -> str:
        # Time: O(1)
        # Space: O(1)
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        s = set(nums)
        if len(s) == 1:
            return "equilateral"
        elif len(s) == 2:
            return "isosceles"
        return "scalene"


