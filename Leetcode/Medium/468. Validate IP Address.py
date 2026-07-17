

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Time: O(n)
        # Space: O(1)
        if "." in queryIP:
            p = queryIP.split(".")
            if len(p) != 4:
                return "Neither"
            for t in p:
                if not t or not t.isdigit() or (len(t) > 1 and t[0] == "0") or int(t) < 0 or int(t) > 255:
                    return "Neither"
            return "IPv4"
        elif ":" in queryIP:
            p = queryIP.split(":")
            if len(p) != 8:
                return "Neither"
            for t in p:
                if len(t) < 1 or len(t) > 4:
                    return "Neither"
                for ch in t:
                    if ch not in "0123456789abcdefABCDEF":
                        return "Neither"
            return "IPv6"
        return "Neither"


