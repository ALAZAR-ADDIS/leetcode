class Solution:
    def bestClosingTime(self, customers: str) -> int:
        Yes=[0]*(len(customers)+1)
        No=[0]*(len(customers)+1)

        for i in range(1,len(Yes)):
            if customers[i-1]=="Y":
                Yes[i]=1
                No[i]=0
            else:
                Yes[i]=0
                No[i]=1
        for i in range(1,len(Yes)):
            Yes[i]=Yes[i-1]+Yes[i]
            No[i]=No[i-1]+No[i]
        Min=0
        val=float("inf")

        for i in range(len(Yes)):
            if val>(No[i]+(Yes[-1]-Yes[i])):
                val=No[i]+(Yes[-1]-Yes[i])
                Min=i

        return Min

        
       