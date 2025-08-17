class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = []
        ans = []
        for i in range(len(mat)):
            arr.append([Counter(mat[i])[1],i])
        heapq.heapify(arr)

        while k > 0:
            count, index = heapq.heappop(arr)
            ans.append(index)
            k -= 1
        return ans
        