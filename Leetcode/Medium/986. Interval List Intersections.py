

class Solution:
    def intervalIntersection(self, firstList: list, secondList: list) -> list:
        # Time: O(n)
        # Space: O(n)
        i, j, out = 0, 0, []
        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i]
            c, d = secondList[j]
            if max(a, c) <= min(b, d):
                out.append([max(a, c), min(b, d)])
            if b < d:
                i += 1
            else:
                j += 1
        return out


        