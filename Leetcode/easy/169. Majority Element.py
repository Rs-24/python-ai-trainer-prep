

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


