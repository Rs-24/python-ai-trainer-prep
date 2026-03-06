from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        n = len(nums)
        return ((n * (n + 1)) // 2) - sum(nums)

# XOR method:
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        

