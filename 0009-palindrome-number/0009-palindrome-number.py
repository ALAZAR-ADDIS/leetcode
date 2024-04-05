class Solution:
    def isPalindrome(self, x: int) -> bool:
        count=0
        x=str(x)
        for i in range(len(x)):
            if x[i]==x[len(x)-1-i]:
                count+=1
        if count==len(x):
            return True
        else:
            return False