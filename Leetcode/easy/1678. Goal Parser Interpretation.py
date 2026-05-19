

class Solution:
    def interpret(self, command: str) -> str:
        # Time: O(n), n = len(command)
        # Space: O(n)
        s = []
        for ch in command:
            if ch == "G":
                s.append(ch)
            elif ch == ")":
                if s[-1] == "(":
                    s[-1] = "o"
                else:
                    l = s.pop()
                    a = s.pop()
                    s.pop()
                    s.append(a)
                    s.append(l)
            else:
                s.append(ch)
        return "".join(s)


