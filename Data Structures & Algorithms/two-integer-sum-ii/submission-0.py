class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in hm:
                return [hm[temp], i+1]
            hm[numbers[i]] = i + 1
        return []