class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0] * l
        for i in range(l):
            ct = temperatures[i]
            for j in range(i+1, l):
                if temperatures[j] > ct:
                    res[i] = j-i
                    break
        return res

        