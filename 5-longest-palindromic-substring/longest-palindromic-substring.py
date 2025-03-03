class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        count = Counter(s)

        
        
        

        for i in range(len(s)-1):
            l = i 
            r = i 



            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > end - start + 1:
                    start = l
                    end = r
                
                l -= 1
                r += 1

            l = i 
            r = i +1 
            
            

            while l >= 0 and r < len(s) and s[l] == s[r]:
                
                if r - l + 1 > end - start + 1:
                    start = l
                    end = r
                
                l -= 1
                r += 1

        return s[start:end + 1]

                
            