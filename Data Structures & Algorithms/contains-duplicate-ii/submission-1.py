class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        ls = len(nums)
        hm = {}

        for i in range(ls):
            if nums[i] in hm and i - hm[nums[i]]<= k:
                return True
            hm[nums[i]]=i
        return False

        