

class Solution:
    def minOperations(self, logs: list) -> int:
        # Time: O(n), n = len(logs)
        # Space: O(1)
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log != "./":
                depth += 1
        return depth


