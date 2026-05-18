class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        ls = len(nums)
        for i in range(ls):
            for j in range(1, ls):
                if i != j and nums[i] == nums[j] and abs(i - j) <= k :
                    return True
        return False
        