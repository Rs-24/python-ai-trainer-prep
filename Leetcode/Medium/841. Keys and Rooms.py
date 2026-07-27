

class Solution:
    def canVisitAllRooms(self, rooms: list[list]) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = set()
        def dfs(r):
            if r in s:
                return
            s.add(r)
            for i in rooms[r]:
                dfs(i)
        dfs(0)
        return len(s) == len(rooms)


        