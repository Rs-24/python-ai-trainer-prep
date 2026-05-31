

class Solution:
    def minOperations(self, nums: list, k: int) -> int:
        # Time: O(n)
        # Space: O(k)
        need = set(x for x in range(1, k + 1))
        have = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in need:
                have.add(nums[i])
            if need == have:
                return len(nums) - i


