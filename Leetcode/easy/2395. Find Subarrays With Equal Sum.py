

class Solution:
    def findSubarrays(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = set()
        cur = nums[0] + nums[1]
        s.add(cur)
        for i in range(2, len(nums)):
            cur += nums[i]
            cur -= nums[i - 2]
            if cur in s:
                return True
            s.add(cur)
        return False


