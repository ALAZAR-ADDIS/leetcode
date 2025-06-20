class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # p = [-i for i in nums]
        # heapq.heapify(p)
        
        # for i in range(k-1):
        #     print(heapq.heappop(p))
        
        
        # return -p[0]
        
        def max_heap(arr, i, end):
            curr = i
            left = 2 * curr + 1
            right = 2 * curr + 2
            if left < end  and arr[left] > arr[curr]:
                curr = left
            
            if right < end and arr[right] > arr[curr]:
                curr = right
            
            if curr != i :
                arr[curr], arr[i] = arr[i], arr[curr]
                max_heap(arr,curr, end)
        
        def heap_pop(arr):
            arr[0], arr[-1] = arr[-1], arr[0]
            arr.pop()
            max_heap(arr,0,len(arr))
        def heapify(arr):
            for i in range(len(arr)//2 - 1, -1 ,-1):
                max_heap(arr, i, len(arr))
        
        heapify(nums)

        for i in range(k- 1):
            heap_pop(nums)
        
        return  nums[0]

        