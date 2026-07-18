class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        s = set(nums)
        s1 = []
        for n in s:
            s1.append(n)
        s1.sort()

        c = 1
        cm = 1
        for i in range(len(s1)-1):
            if s1[i] == (s1[i + 1] - 1):
                c = c + 1
                cm = max(cm, c)
            else:
                c = 1
        return cm
            


        