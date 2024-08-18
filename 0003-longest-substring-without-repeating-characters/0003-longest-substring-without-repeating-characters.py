class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         l=0
#         count={}
#         maxl=0
#         for r in range(len(s)):
#             count[s[r]]=1+count.get(s[r],0)
#             while max(count.values())>1:
#              count[s[l]]=-1+count[s[l]]
#              l+=1
#             maxl=max(maxl,r-l+1)
#         return maxl
#since the time complesity of the max method is higher 
          l=0
          charSet=set()
          maxl=0
          for r in range(len(s)):
            
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            maxl=max(maxl,r-l+1)
          return maxl
          

            