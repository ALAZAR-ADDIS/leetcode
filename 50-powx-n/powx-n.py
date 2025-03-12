class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.solve(x,n)
        else:
            
            return  abs(1 / self.solve(x,abs(n))) * (-1.0 if n % 2 and x < 0 else 1.0)
    

    def solve(self, x , n ):
        if n == 0:
            return 1
        
        if n % 2 == 0 :
            
            return  self.solve(x * x ,n//2)

        else:

            return  x * self.solve(x,n-1)

       
        