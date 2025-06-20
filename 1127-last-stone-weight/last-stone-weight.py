class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def max_heap(arr, i, end):
            curr = i 
            left = curr * 2 + 1
            right = curr * 2 + 2

            if left < end and arr[left] > arr[curr]:
                curr = left
            
            if right < end and arr[right] > arr[curr]:
                curr = right
            
            if curr != i :
                arr[curr], arr[i] = arr[i], arr[curr]
                max_heap(arr, curr, end)
        
        def heapify(arr):
            for i in range(len(arr)//2 - 1 , -1 ,-1):
                max_heap(arr, i, len(arr))
        
        def heap_pop(arr):
            arr[0] ,arr[-1] = arr[-1], arr[0]
            arr.pop()
            max_heap(arr,0, len(arr))
        
        def heap_append(arr,child):

            p = (child - 1) // 2 

            if child > 0 and arr[child] > arr[p]:
                arr[p], arr[child] = arr[child], arr[p]
                heap_append(arr, p)
                
        
        heapify(stones)
        

        while len(stones) > 1:

            max1 =  stones[0]
            heap_pop(stones)
            

            max2 = stones[0]
            heap_pop(stones)

            if max1 != max2:
                stones.append(max1 - max2)
                heap_append(stones, len(stones) - 1)
        
        if stones:
            return stones[0]
        return 0
        