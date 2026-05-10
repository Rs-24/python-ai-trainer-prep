# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/coupon-code-validator/description/

from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Time: O(n * m + n log n), n = len(code) = len(businessLine) = len(isActive), m = len(max(businessLine))
        # Space: O(n)
        order = {"electronics": 1, "grocery": 2, "pharmacy": 3, "restaurant": 4}
        def is_valid_code(s: str) -> bool:
            if not s:
                return False
            for ch in s:
                if not ch.isalnum() and ch != "_":
                    return False
            return True
        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if is_valid_code(c) and b in order and a:
                valid.append((order[b], c))
        valid.sort()
        return [c for _, c in valid]


