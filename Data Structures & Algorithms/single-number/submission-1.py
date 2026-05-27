class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = set()
        for n in nums:
            if n not in res:
                res.add(n)
            else:
                res.remove(n)
        return res.pop()