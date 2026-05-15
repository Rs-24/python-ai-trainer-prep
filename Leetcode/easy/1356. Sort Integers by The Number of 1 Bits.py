

class Solution:
    def sortByBits(self, arr: list) -> list:
        # Time: O(n log M + n log n), n = len(arr), M = max(arr)
        # Space: O(n)
        def one_bits(x: int) -> int:
            count = 0
            while x > 0:
                x &= (x - 1)
                count += 1
            return count
        nums = [(one_bits(num), num) for num in arr]
        nums.sort()
        return [num for _, num in nums]


