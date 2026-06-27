

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        d = {ch: i for i, ch in enumerate(s)}
        st = []
        in_s = set()
        for i, ch in enumerate(s):
            if ch in in_s:
                continue
            while st and st[-1] > ch and d[st[-1]] > i:
                in_s.remove(st.pop())
            st.append(ch)
            in_s.add(ch)
        return "".join(st)


