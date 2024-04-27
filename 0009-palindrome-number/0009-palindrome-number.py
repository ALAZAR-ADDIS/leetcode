class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed=0
        temp=x
        while temp>0:
            reminder=temp%10
            reversed=reversed*10+reminder
            temp=temp//10
        if reversed==x:
            return True
        return False