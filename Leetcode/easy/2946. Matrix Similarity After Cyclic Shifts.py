

class Solution:
    def areSimilar(self, mat: list[list], k: int) -> bool:
        # Time: O(n^2)
        # Space: O(1)
        m, n = len(mat), len(mat[0])
        k %= n
        for idx, r in enumerate(mat):
            i = 0
            j = k if idx % 2 == 0 else n - 1 - k
            while i < n:
                if r[i] != r[j % n]:
                    return False
                i += 1
                j += 1
        return True


