

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Time: O(n)
        # Space: O(n)
        d = {" ": " "}
        i = 0
        for ch in key:
            if ch.isalpha() and ch not in d:
                d[ch] = chr(ord("a") + i)
                i += 1
        return "".join(d[ch] for ch in message)


