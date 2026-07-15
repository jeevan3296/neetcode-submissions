class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        arr = []

        for k1, v1 in hm.items():
            arr.append([v1, k1])
        
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        