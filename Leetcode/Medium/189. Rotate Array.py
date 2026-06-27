

class Solution:
    def rotate(self, nums: list, k: int) -> None:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        k %= n
        def r(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        r(0, n - 1)
        r(0, k - 1)
        r(k, n - 1)


