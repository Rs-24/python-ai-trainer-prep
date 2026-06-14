

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        # Time: O(n)
        # Space: O(n)
        if len(nums) == 1:
            return nums
        l = [nums[0]]
        for i in range(1, len(nums)):
            l.append(max(l[-1], nums[i]))
        r = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            r.append(max(r[-1], nums[i]))
        r.reverse()
        out = []
        for i in range(1, len(nums) - 1):
            if nums[i] > l[i- 1] or nums[i] > r[i + 1]:
                out.append(nums[i])
        return [nums[0]] + out + [nums[-1]]


