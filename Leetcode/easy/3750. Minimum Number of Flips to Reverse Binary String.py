# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/description/

class Solution:
    def minimumFlips(self, n: int) -> int:
        # Time: O(log n)
        # Space: O(log n)
        b = bin(n)[2:]
        m = len(b)
        count = 0
        for i in range(m // 2):
            if b[i] != b[m - i - 1]:
                count += 2
        return count


