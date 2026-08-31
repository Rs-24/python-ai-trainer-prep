

class Solution:
    def sampleStats(self, count: list) -> list:
        # Time: O(1)
        # Space: O(1)
        mi = 0
        while count[mi] == 0:
            mi += 1
        ma = 255
        while count[ma] == 0:
            ma -= 1
        mean = sum(x * count[x] for x in range(256)) / sum(count)
        mode = 0
        for x in range(256):
            if count[x] > count[mode]:
                mode = x
        def f(x):
            t = 0
            for i in range(256):
                t += count[i]
                if t >= x:
                    return i
        if sum(count) % 2 == 1:
            return [mi, ma, mean, f(sum(count) // 2 + 1), mode]
        else:
            return [mi, ma, mean, (f(sum(count) // 2) + f(sum(count) // 2 + 1)) / 2, mode]


