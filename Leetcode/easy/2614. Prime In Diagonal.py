

class Solution:
    def diagonalPrime(self, nums: list[list]) -> int:
        # Time: O(n)
        # Space: O(1)
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            for d in range(2, int(x ** 0.5) + 1):
                if x % d == 0:
                    return False
            return True
        n = len(nums)
        best = 0
        for i in range(n):
            if is_prime(nums[i][i]):
                best = max(best, nums[i][i])
            if is_prime(nums[i][n - i - 1]):
                best = max(best, nums[i][n - i - 1])
        return best


