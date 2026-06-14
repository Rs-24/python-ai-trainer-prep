

class Solution:
    def fourSum(self, nums: list, target: int) -> list[list]:
        # Time: O(n log n + n^3)
        # Space: O(n)
        nums.sort()
        out = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    t = nums[i] + nums[j] + nums[l] + nums[r]
                    if t == target:
                        out.append((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif t < target:
                        l += 1
                    else:
                        r -= 1
        return out


