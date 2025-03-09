class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalG = sum(gas)
        totalC= sum(cost)

        if totalC >totalG:
            return -1
            
        t = 0
        index = 0
        for i in  range(len(gas)):
            if t + gas[i] >= cost[i] :
                t += gas[i] - cost[i]
            else:
                t = 0
                index = i+1
        if index>=len(gas):
            return -1
        return index
    
