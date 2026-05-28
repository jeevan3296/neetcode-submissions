class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        l = len(nums)
        for n in range(l+1):
            if n not in s:
                return n        