class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for k, v in enumerate(nums):
            hm[v] = k

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hm and hm[diff] != i:
                return [i, hm[diff]]

        