

class Solution:
    def canReach(self, arr: list, start: int) -> bool:
        # Time: O(n)
        # Space: O(n)
        stack = [start]
        seen = {start}
        while stack:
            i = stack.pop()
            if arr[i] == 0:
                return True
            for nxt in [i + arr[i], i - arr[i]]:
                if 0 <= nxt < len(arr) and nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return False


