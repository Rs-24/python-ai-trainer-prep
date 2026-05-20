

class Solution:
    def finalValueAfterOperations(self, operations: list) -> int:
        # Time: O(n), n = len(operations)
        # Space: O(1)
        ans = 0
        for op in operations:
            ans += 1 if op[1] == "+" else -1
        return ans


