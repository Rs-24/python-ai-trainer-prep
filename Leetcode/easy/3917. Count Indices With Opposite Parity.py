# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-indices-with-opposite-parity/description/

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        n = len(nums)
        r_even = sum(num % 2 == 0 for num in nums)
        r_odd = n - r_even
        ans = [0] * n
        for i in range(n):
            if nums[i] % 2 == 0:
                r_even -= 1
                ans[i] = r_odd
            else:
                r_odd -= 1
                ans[i] = r_even
        return ans


