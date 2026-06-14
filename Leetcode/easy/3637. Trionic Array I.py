

class Solution:
    def isTrionic(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        if n <= 3:
            return False
        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        t = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == t or i == n - 1:
            return False
        t = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == t:
            return False
        return i == n - 1


