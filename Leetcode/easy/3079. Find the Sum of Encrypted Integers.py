# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/

from typing import List

class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        # Time: O(n * d), n = len(nums), d = average number of digits per word
        # in nums
        # Space: O(1)
        def encrypt(x: int) -> int:
            return int(max(str(x)) * len(str(x)))
        return sum(encrypt(num) for num in nums)


