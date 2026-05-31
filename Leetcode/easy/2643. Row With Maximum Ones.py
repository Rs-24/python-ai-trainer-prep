

class Solution:
    def rowAndMaximumOnes(self, mat: list[list]) -> list:
        # Time: O(n)
        # Space: O(1)
        b, idx = sum(mat[0]), 0
        for i, r in enumerate(mat):
            if sum(r) > b:
                b = sum(r)
                idx = i
        return [idx, b]


