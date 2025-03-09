class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalG = sum(gas)
        totalC= sum(cost)

        if totalC >totalG:
            return -1
        t = 0
        c = 0
        started = False
        index = -1
        for i in  range(len(gas)):
            

            if t + gas[i] >= cost[i] :
                if not started:
                    started = True
                    index = i
                t += gas[i] - cost[i]
            else:
                t = 0
                index = -1
                started = False
        return index
        