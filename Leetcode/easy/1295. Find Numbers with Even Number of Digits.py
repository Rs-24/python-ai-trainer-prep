

class Solution:
    def findNumbers(self, nums: list) -> int:
        # Time: O(n), n = total number of digits in nums
        # Space: O(1)
        count = 0
        for num in nums:
            d = 0
            while num > 0:
                d += 1
                num //= 10
            count += 1 if d % 2 == 0 else 0
        return count 


