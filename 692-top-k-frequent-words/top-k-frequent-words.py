class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count =  Counter(words)
        heap = []
        for x in count:
            heap.append([x,count[x]])
        
        def max_heap(heap, i, end):
            curr = i 
            left =  2 * curr + 1
            right = 2 * curr + 2

            if left < end and heap[left][1] >= heap[curr][1]:
                if (heap[left][1] == heap[curr][1] and heap[left][0] < heap[curr][0]) or  heap[left][1] > heap[curr][1]:
                    curr = left
            if right < end and heap[right][1] >= heap[curr][1]:
                if (heap[right][1] == heap[curr][1] and heap[right][0] < heap[curr][0]) or  heap[right][1] > heap[curr][1]:
                    curr = right
            
            if curr != i:
                heap[curr], heap[i] = heap[i], heap[curr]
                max_heap(heap,curr, end)
        
        def heapify(heap):
            for i in range(len(heap) // 2 - 1, -1 ,-1):
                max_heap(heap,i, len(heap))
        
        def pop_heap(heap):
            heap[0],heap[-1] = heap[-1],heap[0]
            heap.pop()
            max_heap(heap,0,len(heap))

        ans = []     
        heapify(heap)   
        for i in range(k):
            ans.append(heap[0][0])
            pop_heap(heap)

        return ans
                   
                
        