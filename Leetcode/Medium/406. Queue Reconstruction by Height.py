

class Solution:
    def reconstructQueue(self, people: list[list]) -> list[list]:
        # Time: O(n log n)
        # Space: O(n)
        people.sort(key=lambda x: (-x[0], x[1]))
        a = []
        for h, k in people:
            a.insert(k, [h, k])
        return a


