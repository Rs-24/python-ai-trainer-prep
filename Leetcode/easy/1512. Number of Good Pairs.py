

class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        d = {}
        count = 0
        for num in nums:
            if num in d:
                count += d[num]
                d[num] += 1
            else:
                d[num] = 1
        return count


