

class Solution:
    def countBits(self, n: int) -> list[int]:
        # Time: O(n log n)
        # Space: O(n)
        def get_num_ones(x: int) -> int:
            count = 0
            while x > 0:
                x &= (x - 1)
                count += 1
            return count
        return [get_num_ones(x) for x in range(n + 1)]


