

class Solution:
    def countSeniors(self, details: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(int(d[11:13]) > 60 for d in details)


