

class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        f = s = float("inf")
        for x in nums:
            if x <= f:
                f = x
            elif x <= s:
                s = x
            else:
                return True
        return False


