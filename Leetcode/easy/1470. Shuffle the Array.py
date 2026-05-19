

class Solution:
    def shuffle(self, nums: list, n: int) -> list:
        # Time: O(n)
        # Space: O(n)
        out = []
        for i in range(n):
            out.append(nums[i])
            out.append(nums[i + n])
        return out


