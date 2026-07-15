class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        freq = [[] for _ in range(len(nums)+1)]

        for k1, v1 in hm.items():
            freq[v1].append(k1)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        