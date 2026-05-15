

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        out = [0] * n
        insert_pos = n - 1
        l, r = 0, n - 1
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                out[insert_pos] = nums[r] * nums[r]
                r -= 1
            else:
                out[insert_pos] = nums[l] * nums[l]
                l += 1
            insert_pos -= 1
        return out


