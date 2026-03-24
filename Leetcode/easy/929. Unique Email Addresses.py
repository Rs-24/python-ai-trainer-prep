# Time to write all of below including tests, explanation and time and aux
# and total space: 7 mins

# Problem: https://leetcode.com/problems/unique-email-addresses/description/

from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Time: O(n), n = total number of characters in emails
        # Space: O(n)
        unique = set()
        for email in emails:
            temp = []
            plus = at = False
            for ch in email:
                if ch == "+":
                    plus = True
                elif ch == ".":
                    if at:
                        temp.append(ch)
                else:
                    if ch == "@":
                        plus = False
                        at = True
                    if not plus:
                        temp.append(ch)
            unique.add("".join(temp))
        return len(unique)


