class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftpointer=0
        rightpointer=len(s)-1
        while rightpointer>leftpointer:
           s[rightpointer],s[leftpointer]=s[leftpointer],s[rightpointer]
           rightpointer-=1
           leftpointer+=1
        return s;
           
            

        