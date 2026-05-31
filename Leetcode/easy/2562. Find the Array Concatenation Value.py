

class Solution:
    def findTheArrayConcVal(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        def join(x1: int, x2: int) -> int:
            m = 10
            while m <= x2:
                m *= 10
            return x1 * m + x2
        s = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                s += nums[l]
                break
            s += join(nums[l], nums[r])
            l += 1
            r -= 1
        return s


