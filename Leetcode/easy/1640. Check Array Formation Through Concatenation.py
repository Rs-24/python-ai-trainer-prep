

class Solution:
    def canFormArray(self, arr: list, pieces: list[list]) -> bool:
        # Time: O(m + n), m = len(arr), n = len(pieces)
        # Space: O(n)
        d = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            p = d[arr[i]]
            for num in p:
                if i >= len(arr) or num != arr[i]:
                    return False
                i += 1
        return True


