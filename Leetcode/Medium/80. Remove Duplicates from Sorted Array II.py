

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        i = 0
        for x in nums:
            if i < 2 or x != nums[i - 2]:
                nums[i] = x
                i += 1
        return i


