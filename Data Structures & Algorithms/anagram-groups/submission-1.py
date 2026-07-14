class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            can = ''.join(sorted(s))
            res[can].append(s)
        return list(res.values())



        