

class Solution:
    def secondHighest(self, s: str) -> int:
        # Time: O(n), n = len(s)
        # Space: O(1)
        nums = set(int(ch) for ch in s if ch.isdigit())
        if len(nums) < 2:
            return -1
        nums.remove(max(nums))
        return max(nums)


