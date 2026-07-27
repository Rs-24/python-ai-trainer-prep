

class Solution:
    def advantageCount(self, nums1: list, nums2: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        nums1.sort()
        t = sorted((x, i) for i, x in enumerate(nums2))
        a = [0] * len(nums1)
        l, r = 0, len(nums1) - 1
        for x in reversed(nums1):
            if x > t[r][0]:
                i = t[r][1]
                a[i] = x
                r -= 1
            else:
                i = t[l][1]
                a[i] = x
                l += 1
        return a


        