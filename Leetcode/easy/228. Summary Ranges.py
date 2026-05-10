

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        out = []
        n = len(nums)
        i = 0
        while i < n:
            a = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            b = nums[i]
            if a == b:
                out.append(str(a))
            else:
                out.append(str(a) + "->" + str(b))
            i += 1
        return out


