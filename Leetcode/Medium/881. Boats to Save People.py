

class Solution:
    def numRescueBoats(self, people: list, limit: int) -> int:
        # Time: O(n log n)
        # Space: O(1)
        people.sort()
        l, r = 0, len(people) - 1
        t = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            t += 1
        return t


        