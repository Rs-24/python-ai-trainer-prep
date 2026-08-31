

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        d = {ch: i for i, ch in enumerate(s)}
        st = []
        seen = set()
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while (st and st[-1] > ch and d[st[-1]] > i):
                seen.remove(st.pop())
            st.append(ch)
            seen.add(ch)
        return "".join(st)


