

class Solution:
    def dayOfYear(self, date: str) -> int:
        # Time: O(1)
        # Space: O(1)
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:10])
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
            months[1] = 29
        for i in range(m - 1):
            d += months[i]
        return d


