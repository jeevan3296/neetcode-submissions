class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for n in range(n+1):
            r1 = self.ones(n)
            res.append(r1)
        return res
        
    def ones(self, a: int) -> int:
        count = 0

        while a:
            a = a & (a-1)
            count += 1
        return count

        