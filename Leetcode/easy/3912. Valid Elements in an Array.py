# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/valid-elements-in-an-array/description/

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        if n <= 2:
            return nums
        l_max = nums[0]
        r_max = [0] * n
        r_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            r_max[i] = max(nums[i], r_max[i + 1])
        out = []
        for i in range(1, n - 1):
            if nums[i] > l_max and nums[i] > r_max[i]:
                out.append(nums[i])
            l_max = max(l_max, nums[i])
        return [nums[0]] + out + [nums[-1]]


