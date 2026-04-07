# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/

from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        distance = -1
        for num in nums:
            if num == 1:
                if distance == -1:
                    distance = 0
                else:
                    if distance < k:
                        return False
                    distance = 0
            else:
                if distance != -1:
                    distance += 1
        return True


