

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        # Time: O(n)
        # Space: O(1)
        i = 0
        num = None
        c = 0
        for n in nums:
            if n == num:
                c += 1
            else:
                num = n
                c = 1
            if c <= k:
                nums[i] = num
                i += 1
        return nums[:i]


