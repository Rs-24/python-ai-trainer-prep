# Time to write all of below including tests, explanation and time and aux
# and total space: 24 mins

# Problem: https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        for i in range(n):
            if i == 0:
                continue
            out[i] = out[i - 1] * nums[i - 1]
        i = n - 2
        product = 1
        while i >= 0:
            product *= nums[i + 1]
            out[i] *= product
            i -= 1
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.productExceptSelf([1, 2]) == [2, 1]
    assert sol.productExceptSelf([-1, 0, 1]) == [0, -1, 0]
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert sol.productExceptSelf([1, -1, 2, -4]) == [8, -8, 4, -2]

# Explanation: the code creates the list 'out', which initially stores only one's,
# and then makes one pass through nums and sets each element in out to the
# product of every element in nums before the same index. Then it makes
# another pass through nums from the end, and multiplies each element in out
# by the product of the elements in nums after the same index.
# Time: O(n), n = len(nums)
# Space: excluding output: O(1)


