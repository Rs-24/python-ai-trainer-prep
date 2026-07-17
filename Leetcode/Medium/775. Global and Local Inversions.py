

class Solution:
    def isIdealPermutation(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        t = nums[0]
        for i in range(2, len(nums)):
            t = max(t, nums[i - 2])
            if t > nums[i]:
                return False
        return True


        