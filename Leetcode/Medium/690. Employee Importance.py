

class Employee:
    def __init__(self, id: int, importance: int, subordinates: list):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: list, id: int) -> int:
        # Time: O(n)
        # Space: O(n)
        d = {e.id: e for e in employees}
        a = 0
        s = [id]
        while s:
            e = d[s.pop()]
            a += e.importance
            s.extend(e.subordinates)
        return a


