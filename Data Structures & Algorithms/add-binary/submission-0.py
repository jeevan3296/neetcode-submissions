class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # list
        # sum, carry
        res = []
        carry = 0
        i = len(a)-1
        j = len(b)-1
        while i >= 0 or j >= 0 or carry>0 :
            a1 = int(a[i]) if i >= 0 else 0
            b1 = int(b[j]) if j >= 0 else 0

            sum = (a1+b1+carry)
            res.append(sum%2)
            carry = sum//2

            i-=1
            j-=1
        
        return ''.join(str(x) for x in res[::-1])
            



        # return reverse list, for each val, convert to str
        