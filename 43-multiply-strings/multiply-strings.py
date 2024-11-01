class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=0
        n2=0
        for i in num1:
            n1*=10
            n1=n1+ord(i)-ord("0")
        for i in num2:
            n2*=10
            n2=n2+ord(i)-ord("0")
        return f"{n1*n2}"
        
        