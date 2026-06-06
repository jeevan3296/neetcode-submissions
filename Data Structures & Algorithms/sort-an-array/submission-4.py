class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range((n-2)//2, -1, -1):
            self.siftDown(nums, i, n)

        for end in range(n-1, 0, -1):
            nums[0],nums[end] = nums[end], nums[0]
            self.siftDown(nums, 0, end)
        return nums
    

    def siftDown(self, arr, i, n):
        while True:
            l = (2*i)+1
            r = (2*i)+2
            largest = i

            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if i == largest:
                return
            
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest