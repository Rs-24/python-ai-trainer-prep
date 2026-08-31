

class Solution:
    def corpFlightBookings(self, bookings: list, n: int) -> list:
        # Time: O(n + len(bookings))
        # Space: O(n)
        d = [0] * n
        for f, l, s in bookings:
            d[f - 1] += s
            if l < n:
                d[l] -= s
        for i in range(1, n):
            d[i] += d[i - 1]
        return d


