class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
        
        sorted_pair = sorted(hm.items(), key = lambda x : -x[1])

        res = [k for k, v in sorted_pair[:k]]

        return res