# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/decode-the-message/description/

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # Time: O(m + n), m = len(key), n = len(message)
        # Aux space: O(1)
        d = {}
        i = 0
        for ch in key:
            if ch.isalpha() and ch not in d:
                d[ch] = chr(ord("a") + i)
                i += 1
        out = []
        for ch in message:
            out.append(d[ch]) if ch in d else out.append(ch)
        return "".join(out)


