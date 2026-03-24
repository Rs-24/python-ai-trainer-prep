# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/number-of-lines-to-write-string/description/

from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # Time: O(n), n = len(s)
        # Space, excluding output: O(1)
        num_lines = 1
        current_width = 0
        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if current_width + w > 100:
                num_lines += 1
                current_width = w
            else:
                current_width += w
        return [num_lines, current_width]


