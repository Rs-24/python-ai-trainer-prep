

class Solution:
    def sortColors(self, nums: list) -> None:
        # Time: O(n)
        # Space: O(1)
        l, r, c = 0, len(nums) - 1, 0
        while c <= r:
            if nums[c] == 0:
                nums[l], nums[c] = nums[c], nums[l]
                l += 1
                c += 1
            elif nums[c] == 2:
                nums[r], nums[c] = nums[c], nums[r]
                r -= 1
            else:
                c += 1


