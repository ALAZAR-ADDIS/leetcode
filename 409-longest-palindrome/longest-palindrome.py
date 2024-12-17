# class Solution:
#     def longestPalindrome(self, s: str) -> int:
        
#         wordFreq={}
#         total=0
#         for i in s:
#             wordFreq[i]=wordFreq.get(i,0)+1
#             if wordFreq[i]%2==0:
#                 total+=2
        

#         for i in wordFreq.values():
#             if i%2!=0:
#                total+=1
#                break
#         return total 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        wordFreq={}
        for i in s:
            wordFreq[i]=wordFreq.get(i,0)+1
        total=0
        maxOdd=0

        print(wordFreq)
        for i in wordFreq.values():
            print(i)
            if i%2:
               
                if maxOdd<=i:
                    total+=maxOdd-1 if maxOdd else 0
                    maxOdd=i
                   
                else:
                    total+=i-1
                continue
        
            total+=i
            print(total)
        print(maxOdd)
        print(total)
        return total + maxOdd
            
            
                

        