# 100

def climbing_stairs(n: int) -> int:
    if n <= 2:
        return n
    prev = 2
    prev_prev = 1
    total = 0
    for i in range(3, n//2):
        total += (prev + prev_prev + 1)
        prev_prev = prev
        prev = total


        # one 2: n-1

        # two 2's:
        # 4 -> 1
        # 5 -> 2 + 1
        # 6 -> 3 + 2 + 1
        # 7 -> 4 + 3 + 2 + 1
        # 8 -> 5 + 4 + 3 + 2 + 1

        # three 2's:
        # 6 -> 1
        # 7 -> 3 + 1
        # 8 -> 6 + 3 + 1
        # 9 -> 10 + 6 + 3 + 1
        # 10 -> 15 + 10 + 6 + 3 + 1

        # four 2's:
        # 8 -> 1
        # 9 -> 4 + 1
        # 10 -> 10 + 4 + 1
        # 11 -> 20 + 10 + 4 + 1
        # 12 -> 35 + 20 + 10 + 4 + 1
        
    



