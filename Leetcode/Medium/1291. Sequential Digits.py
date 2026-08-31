

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list:
        # Time: O(n)
        # Space: O(n)
        ans = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(1, 10 - length):
                num = 0
                for digit in range(start, start + length):
                    num = num * 10 + digit
                if low <= num <= high:
                    ans.append(num)
        return ans


