

class Solution:
    def findIndices(self, nums: list, indexDifference: int, valueDifference: int) -> list:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        min_i = max_i = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[i] > nums[max_i]:
                max_i = i
            if abs(nums[min_i] - nums[j]) >= valueDifference:
                return [min_i, j]
            if abs(nums[max_i] - nums[j]) >= valueDifference:
                return [max_i, j]
        return [-1, -1]


