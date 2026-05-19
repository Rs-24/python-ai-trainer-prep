

class Solution:
    def reformatNumber(self, number: str) -> str:
        # Time: O(n), n = len(number)
        # Space: O(n)
        n = []
        for ch in number:
            if ch.isdigit():
                n.append(ch)
        groups = []
        while len(n) > 4:
            groups.append("".join(n[:3]))
            n = n[3:]
        if len(n) <= 3:
            groups.append("".join(n))
        else:
            groups.append("".join(n[:2]))
            groups.append("".join(n[2:]))
        return "-".join(groups)


