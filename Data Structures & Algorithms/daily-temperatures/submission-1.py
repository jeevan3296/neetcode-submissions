class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        res = [0] * l
        unanswered = []
        for i, t in enumerate(temperatures):
            while unanswered and t > temperatures[unanswered[-1]]:
                j = unanswered.pop()
                res[j] = i - j
            unanswered.append(i)
        return res

        