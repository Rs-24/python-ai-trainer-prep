

class Solution:
    def countMatches(self, items: list[list], ruleKey: str, ruleValue: str) -> int:
        # Time: O(n), n = len(items)
        # Space: O(1)
        count = 0
        for i in items:
            t, c, n = i
            if ruleKey == "type" and ruleValue == t:
                count += 1
            elif ruleKey == "color" and ruleValue == c:
                count += 1
            elif ruleKey == "name" and ruleValue == n:
                count += 1
        return count


