

class Solution:
    def pancakeSort(self, arr: list) -> list:
        # Time: O(n^2)
        # Space: O(n)
        a, n = [], len(arr)
        for x in range(n, 1, -1):
            i = arr.index(x)
            if i == x - 1:
                continue
            if i != 0:
                arr[:i + 1] = reversed(arr[:i + 1])
                a.append(i + 1)
            arr[:x] = reversed(arr[:x])
            a.append(x)
        return a


        