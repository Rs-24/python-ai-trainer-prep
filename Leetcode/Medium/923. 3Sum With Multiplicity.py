

class Solution:
    def threeSumMulti(self, arr: list, target: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        arr.sort()
        a = 0
        for i in range(len(arr) - 2):
            l, r = i + 1, len(arr) - 1
            while l < r:
                if arr[l] + arr[r] < target - arr[i]:
                    l += 1
                elif arr[l] + arr[r] > target - arr[i]:
                    r -= 1
                else:
                    if arr[l] != arr[r]:
                        lc = rc = 1
                        while l + 1 < r and arr[l] == arr[l + 1]:
                            lc += 1
                            l += 1
                        while r - 1 > l and arr[r] == arr[r - 1]:
                            rc += 1
                            r -= 1
                        a += lc * rc
                        l += 1
                        r -= 1
                    else:
                        t = r - l + 1
                        a += t * (t - 1) // 2
                        break
        return a % (10 ** 9 + 7)


        