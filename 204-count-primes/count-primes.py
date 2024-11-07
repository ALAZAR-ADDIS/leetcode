class Solution:
    def countPrimes(self, n: int) -> int:
        count=[1 for i in range(n+1)]
        ans=0

        for i in range(2,n):
            if count[i]:
                for j in range(i*i,n,i):
                    count[j]=0
        for i in range(3,n+1):
            if count[i]:
                ans+=1
        return ans
    
    def isPrime(num):
        
        for i in range(2,num//2+1):
            if num%i==0:
                return False
        return True
    



        