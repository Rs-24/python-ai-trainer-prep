

class Solution:
    def mergeArrays(self, nums1: list[list], nums2: list[list]) -> list[list]:
        # Time: O(n)
        # Space: O(n)
        i = j = 0
        out = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                out.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                out.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                out.append([nums2[j][0], nums2[j][1]])
                j += 1
        out.extend(nums1[i:])
        out.extend(nums2[j:])
        return out


