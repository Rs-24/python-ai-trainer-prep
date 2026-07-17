

class Solution:
    def checkPossibility(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        t = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if t:
                    return False
                t = True
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        return True


