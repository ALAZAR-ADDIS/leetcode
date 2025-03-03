class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = []
        total = 0
        for start , end in costs:
            cost.append((end - start,start,end))

        
        
        cost.sort(key = lambda x:x[0])
        mid = len(cost)//2

        for i in range(mid):
            total += cost[i][2]
           


        for i in range(mid,len(cost)):
             total += cost[i][1]
        
        return total

        
        