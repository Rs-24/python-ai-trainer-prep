# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/xor-operation-in-an-array/description/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # Time: O(n)
        # Space: O(1)
        ans = start
        for i in range(1, n):
            ans ^= (start + 2 * i)
        return ans


