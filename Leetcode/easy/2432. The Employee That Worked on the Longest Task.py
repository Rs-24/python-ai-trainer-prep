

class Solution:
    def hardestWorker(self, n: int, logs: list[list]) -> int:
        # Time: O(n), n = len(logs)
        # Space: O(1)
        prev = 0
        best_id = logs[0][0]
        best_time = 0
        for a, b in logs:
            if b - prev > best_time:
                best_time = b - prev
                best_id = a
            elif b - prev == best_time:
                best_id = min(best_id, a)
            prev = b
        return best_id


