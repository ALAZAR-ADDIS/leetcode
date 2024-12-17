class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        wordFreq={}
        total=0
        for i in s:
            wordFreq[i]=wordFreq.get(i,0)+1
            if wordFreq[i]%2==0:
                total+=2
        

        for i in wordFreq.values():
            if i%2!=0:
               total+=1
               break
        return total 
            
                

        