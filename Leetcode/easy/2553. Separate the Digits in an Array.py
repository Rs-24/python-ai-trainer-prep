

class Solution:
    def separateDigits(self, nums: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        def separate(x: int) -> list:
            if x == 0:
                return [0]
            d = []
            while x > 0:
                d.append(x % 10)
                x //= 10
            d.reverse()
            return d
        out = []
        for num in nums:
            out.extend(separate(num))
        return out


