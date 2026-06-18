

class Solution:
    def subsetsWithDup(self, nums: list) -> list[list]:
        # Time: O(n * (2 ** n))
        # Space: O(2 ** n)
        nums.sort()
        out = [[]]
        p = 0
        for i, x in enumerate(nums):
            s = p if i > 0 and nums[i] == nums[i - 1] else 0
            p = len(out)
            for j in range(s, p):
                out.append(out[j] + [x])
        return out

