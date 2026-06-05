import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.sortq(nums, 0, len(nums)-1)
        return nums


    def sortq(self, arr, lo, hi):
        if lo >= hi:
            return
        # find pivot
        pivot_idx = random.randint(lo, hi)
        arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
        pivot = arr[hi]
        # lumuto partition strategy

        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i],arr[j] = arr[j], arr[i]
                i+=1
        arr[i], arr[hi] = arr[hi], arr[i]

        # recursion of before and after pivot
        self.sortq(arr, lo, i-1)
        self.sortq(arr, i+1, hi)

        