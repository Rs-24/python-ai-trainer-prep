

class Solution:
    def countPairs(self, nums: list, k: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count


