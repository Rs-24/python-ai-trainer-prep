

class Solution:
    def numFriendRequests(self, ages: list) -> int:
        # Time: O(n log n)
        # Space: O(1)
        ages.sort()
        n = len(ages)
        a = 0
        l = r = 0
        for i in range(n):
            if ages[i] < 15:
                continue
            while ages[l] <= 0.5 * ages[i] + 7:
                l += 1
            while r + 1 < n and ages[r + 1] <= ages[i]:
                r += 1
            a += r - l
        return a


