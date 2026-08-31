

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        st = []
        for ch in s:
            if st and st[-1][0] == ch:
                st[-1][1] += 1
            else:
                st.append([ch, 1])
            if st and st[-1][1] == k:
                st.pop()
        return "".join(ch * f for ch, f in st)


