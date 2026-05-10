

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        # Time: O(1)
        # Space: O(1)
        out = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    m = "0" + str(m) if m < 10 else str(m)
                    out.append(str(h) + ":" + m)
        return out


