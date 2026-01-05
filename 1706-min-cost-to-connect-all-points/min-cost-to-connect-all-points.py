class unionFind:
    def __init__(self,size):
        self.parent = {i:i for i in range(size)}

    def find(self,x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        par_x = self.find(x)
        par_y = self.find(y)

        if par_x != par_y:
            self.parent[par_x] = par_y

    def connected(self, x,y):
        return self.find(x) == self.find(y)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uni = unionFind(len(points))
        heap = []
        for index,valu in enumerate(points):
            for index2,valu2 in enumerate(points):
                if index2 > index:
                    hyp = abs(valu[0] - valu2[0])  + abs(valu[1] - valu2[1])
                    heappush(heap,(hyp,index,index2))
       
        ans = 0
        n = 0
        while  n < len(points) - 1:
            w,n1,n2 = heappop(heap)
            if uni.connected(n1,n2):
                continue
            
            print(n1,n2,w)
            print(uni.parent[n1], uni.parent[n2],"added")
            uni.union(n1,n2)
            n += 1
            ans += w
      
        return ans

        