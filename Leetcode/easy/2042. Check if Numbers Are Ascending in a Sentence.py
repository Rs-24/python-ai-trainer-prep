

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        prev = None
        cur = None
        for ch in s:
            if ch.isdigit():
                if cur is None:
                    cur = int(ch)
                else:
                    cur = cur * 10 + int(ch)
            else:
                if prev is not None and cur is not None and prev >= cur:
                        return False
                prev = cur
                cur = None
        if prev is not None and cur is not None and prev >= cur:
            return False
        return True


