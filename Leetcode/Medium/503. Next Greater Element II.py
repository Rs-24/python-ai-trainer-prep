

class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        a = [-1] * n
        s = []
        for i in range(2 * n):
            while s and nums[s[-1]] < nums[i % n]:
                j = s.pop()
                a[j] = nums[i % n]
            if i < n:
                s.append(i)
        return a


