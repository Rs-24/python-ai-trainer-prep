


class Solution:
    def totalNumbers(self, digits: list) -> int:
        # Time: O(n^3)
        # Space: O(n)
        s = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            for j in range(len(digits)):
                if i == j:
                    continue
                for k in range(len(digits)):
                    if i == k or j == k or digits[k] % 2 != 0:
                        continue
                    s.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(s)


