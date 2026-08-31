

class Solution:
    def addNegabinary(self, arr1: list, arr2: list) -> list:
        # Time: O(n)
        # Space: O(n)
        i, j, c, a = len(arr1) - 1, len(arr2) - 1, 0, []
        while i >= 0 or j >= 0 or c:
            t = c
            if i >= 0:
                t += arr1[i]
                i -= 1
            if j >= 0:
                t += arr2[j]
                j -= 1
            a.append(t & 1)
            c = -(t >> 1)
        a.reverse()
        while len(a) > 1 and a[0] == 0:
            a.pop(0)
        return a


