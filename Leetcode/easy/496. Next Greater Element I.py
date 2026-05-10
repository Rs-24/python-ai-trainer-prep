

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Space: O(m + n)
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        out = []
        for num in nums1:
            if num in next_greater:
                out.append(next_greater[num])
            else:
                out.append(-1)
        return out


