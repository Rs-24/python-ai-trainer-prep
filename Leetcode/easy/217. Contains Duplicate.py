

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


