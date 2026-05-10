
 
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time: O(m + n), m = len(a), n = len(b)
        # Space: O(m + n)
        a_len, b_len = len(a), len(b)
        if a_len < b_len:
            a = "0" * (b_len - a_len) + a
        elif a_len > b_len:
            b = "0" * (a_len - b_len) + b
        a, b = a[::-1], b[::-1]
        out = []
        carry = 0
        for i in range(len(a)):
            d = int(a[i]) + int(b[i]) + carry
            out.append(str(d % 2))
            carry = d // 2
        if carry:
            out.append("1")
        return "".join(reversed(out))


