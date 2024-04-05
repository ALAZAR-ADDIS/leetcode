class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num=[]
        for i in range(1,n+1):
            num.append(i)
        k=k-1
        startindex=0
        while len(num)>1:
            toberemoved=(startindex+k)%len(num)
            num.pop(toberemoved)
            startindex=toberemoved
        return num[0]

            
