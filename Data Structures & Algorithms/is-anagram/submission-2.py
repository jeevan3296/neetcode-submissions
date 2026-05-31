class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)

        if sl != tl:
            return False

        cs = {}
        ct = {}
        
        for i in range(0, sl):
            cs[s[i]] = 1 + cs.get(s[i], 0)
            ct[t[i]] = 1 + ct.get(t[i], 0)
        return cs == ct

        