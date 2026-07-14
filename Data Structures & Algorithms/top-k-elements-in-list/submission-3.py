class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequencies using hm
        hm = {}

        for n in nums:
            hm[n] = 1 + hm.get(n, 0)

        # convert to and sort the array
        arr = []
        for k1, v in hm.items():
            arr.append([v, k1])
        arr.sort()

        # pop the array values alone

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        