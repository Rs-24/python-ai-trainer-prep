

def rand7():
    pass

class Solution:
    def rand10(self):
        # Time: O(1)
        # Space: O(1)
        while True:
            x = (rand7() - 1) * 7 + rand7()
            if x <= 40:
                return (x - 1) % 10 + 1


