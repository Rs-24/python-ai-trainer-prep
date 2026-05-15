

class Solution:
    def kLengthApart(self, nums: list, k: int) -> bool:
        # Time: O(n), n = len(nums)
        # Space: O(1)
        d = -1
        for num in nums:
            if num == 0:
                if d != -1:
                    d += 1
            else:
                if d == -1:
                    d = 0
                else:
                    if d < k:
                        return False
                    d = 0
        return True


