

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        # Time: O(n), n = total number of characters in emails
        # Space: O(n)
        s = set()
        for e in emails:
            l, d = e.split("@")
            l = l.replace(".", "")
            i = l.find("+")
            if i != -1:
                l = l[:i]
            s.add(l + "@" + d)
        return len(s)


