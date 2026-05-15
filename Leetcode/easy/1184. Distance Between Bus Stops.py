

class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        # Time: O(n), n = len(distance)
        # Space: O(1)
        if start > destination:
            start, destination = destination, start       
        c = 0
        for i in range(start, destination):
            c += distance[i]
        return min(c, sum(distance) - c)


