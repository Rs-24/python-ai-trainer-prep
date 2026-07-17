

class Solution:
    def triangleNumber(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(1)
        nums.sort()
        n = len(nums)
        a = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    a += j - i
                    j -= 1
                else:
                    i += 1
        return a


