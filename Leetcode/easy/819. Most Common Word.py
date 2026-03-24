# Time to write all of below including tests, explanation and time and aux
# and total space: 5 mins

# Problem: https://leetcode.com/problems/most-common-word/description/

from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Time: O(m + n), m = len(paragraph), n = len(banned)
        # Space: O(m + n)
        banned = set(banned)
        paragraph = re.findall(r"[a-zA-Z]+", paragraph.lower())
        c = Counter(word for word in paragraph if word not in banned)
        return c.most_common(1)[0][0]


