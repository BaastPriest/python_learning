class Solution:
    def fib(self, n: int) -> int:
        numfib = 0
        f1, f2 = 1, 0
        if n ==0:
            return 0
        elif n ==1:
            return 1
        else:
            for i in range(2, n+1):
                numfib = f1 + f2
                f1, f2 = f1+ f2, f1
            return numfib
