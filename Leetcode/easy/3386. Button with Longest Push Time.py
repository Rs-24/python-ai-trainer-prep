

class Solution:
    def buttonWithLongestTime(self, events: list[list]) -> int:
        # Time: O(n)
        # Space: O(1)
        ans = events[0][0]
        b = events[0][1]
        for i in range(1, len(events)):
            if events[i][1] - events[i - 1][1] > b:
                b = events[i][1] - events[i - 1][1]
                ans = events[i][0]
            elif events[i][1] - events[i - 1][1] == b and events[i][0] < ans:
                ans = events[i][0]
        return ans


