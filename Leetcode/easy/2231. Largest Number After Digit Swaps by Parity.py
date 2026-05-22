

class Solution:
    def largestInteger(self, num: int) -> int:
        # Time: O(n log n)
        # Space: O(log n)
        e = sorted([int(d) for d in str(num) if int(d) % 2 == 0], reverse=True)
        o = sorted([int(d) for d in str(num) if int(d) % 2 != 0], reverse=True)
        out = []
        i = j = 0
        for d in str(num):
            if int(d) % 2 == 0:
                out.append(e[i])
                i += 1
            else:
                out.append(o[j])
                j += 1
        return int("".join(out))


