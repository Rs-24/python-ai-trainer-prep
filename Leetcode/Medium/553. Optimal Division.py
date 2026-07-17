

class Solution:
    def optimalDivision(self, nums: list) -> str:
        # Time: O(n)
        # Space: O(n)
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        return str(nums[0]) + "/(" + "/".join(map(str, nums[1:])) + ")"


