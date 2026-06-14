

class Solution:
    def validateCoupons(self, code: list, businessLine: list, isActive: list) -> list:
        # Time: O(n log n)
        # Space: O(n)
        v = []
        order = {"electronics": 1, "grocery": 2, "pharmacy": 3, "restaurant": 4}
        for c, b, a in zip(code, businessLine, isActive):
            if c and all(ch.isalnum() or ch == "_" for ch in c) and b in order and a:
                v.append((order[b], c))
        v.sort()
        return [c for _, c in v]


