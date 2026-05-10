# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-least-frequent-digit/description/

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(1)
        count = [0] * 10
        while n > 0:
            count[n % 10] += 1
            n //= 10
        ans = 0
        min_freq = float("inf")
        for digit, freq in enumerate(count):
            if 0 < freq < min_freq:
                ans = digit
                min_freq = freq
        return ans


