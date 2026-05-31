

class Solution:
    def differenceOfSum(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        def sum_digits(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s
        return abs(sum(nums) - sum(sum_digits(num) for num in nums))


