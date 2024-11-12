class Solution:
    def reverse(self, x: int) -> int:
        
        
        y=-x if x<0 else x
        
        rev=0
        while y:
            rem=y%10
            y=(y//10)
            rev+=rem
            rev*=10
        rev=rev//10
        if rev<-2**31 or rev>(2**31-1 ):
            return 0
        
        return -rev if x<0 else rev
            

        