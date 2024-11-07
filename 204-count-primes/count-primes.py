class Solution:
    def countPrimes(self, n: int) -> int:
        count=[1 for i in range(n+1)]
        ans=0

        for i in range(2,n):
            if math.ceil(sqrt(n))<=i:
                break
            if count[i]:
                for j in range(i*i,n,i):
                    count[j]=0
    
        for i in range(2,n):
            if count[i]:
                ans+=1
        return ans
    
   
    



        