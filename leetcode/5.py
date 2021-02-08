class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a=1
        b=0
        for i in str(n):
            a*=int(i)
            b+=int(i)
            x=a-b
        return x