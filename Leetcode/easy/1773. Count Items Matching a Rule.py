# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/count-items-matching-a-rule/description/

from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Time: O(n), n = len(items)
        # Space: O(1)
        total = 0
        for item in items:
            type_, color, name = item
            if ruleKey == "type" and type_ == ruleValue:
                total += 1
            elif ruleKey == "color" and color == ruleValue:
                total += 1
            elif ruleKey == "name" and name == ruleValue:
                total += 1
        return total


