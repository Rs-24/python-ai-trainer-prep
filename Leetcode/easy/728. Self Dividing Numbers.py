

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        # Time: O(n log right), n = right - left + 1
        # Space: O(n)
        def check(x: int) -> bool:
            original = x
            while x > 0:
                if x % 10 == 0 or original % (x % 10) != 0:
                    return False
                x //= 10
            return True
        return [num for num in range(left, right + 1) if check(num)]


