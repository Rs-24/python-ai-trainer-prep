

class Solution:
    def findDuplicates(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        a = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                a.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return a


