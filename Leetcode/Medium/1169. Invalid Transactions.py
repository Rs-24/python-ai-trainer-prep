

class Solution:
    def invalidTransactions(self, transactions: list) -> list:
        # Time: O(n^2)
        # Space: O(n)
        a = []
        for i, tr1 in enumerate(transactions):
            n1, t1, am1, c1 = tr1.split(",")
            if int(am1) > 1000:
                a.append(tr1)
            else:
                for j, tr2 in enumerate(transactions):
                    if i != j:
                        n2, t2, am2, c2 = tr2.split(",")
                        if n1 == n2 and abs(int(t1) - int(t2)) <= 60 and c1 != c2:
                            a.append(tr1)
                            break
        return a


