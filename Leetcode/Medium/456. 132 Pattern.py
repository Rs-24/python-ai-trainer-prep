

class Solution:
    def find132pattern(self, nums: list) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = []
        two = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < two:
                return True
            while s and nums[i] > s[-1]:
                two = s.pop()
            s.append(nums[i])
        return False


