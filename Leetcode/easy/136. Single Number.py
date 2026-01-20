# Time to write all of below including tests, explanation and time and aux 
# space: 32 mins

# I needed help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/single-number/description/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x = 0
        for num in nums:
            x ^= num
        return x

if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([1]) == 1
    assert sol.singleNumber([2, 2]) == 0
    assert sol.singleNumber([-1, 0, 3, -1, 0]) == 3

# Explanation: XOR is used with each digit
# Time: O(n), n = len(nums)
# Aux space excluding output and input: O(1)
# Total space including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 32 mins):
#   - The "assert sol.singleNumber([2, 2]) == 0" test isn't really valid for
#     Leetcode constraints. I could have replaced it with e.g.
#     "assert sol.singleNumber([2, 2, 1]) == 1"
#   - Additionally, I could have improved my explanation a bit. My rewrite is
#     below:

# Explanation: XOR is used with each element in nums, whereby 0 ^ num = num and 
# num ^ num = 0






