class Solution:
    def validPalindrome(self, s: str) -> bool:
        # l_dif=0
        # r_dif = 0
        # l = 0
        # r = len(s) - 1

        # while l<r:
        #     if s[l] == s[r]:
        #         l+=1
        #         r -= 1
        #     else:
        #         l += 1
        #         l_dif +=1

        # if l_dif <= 1:       
        #     return True

        # l = 0
        # r = len(s) - 1

        # while l<r:
        #     if s[l] == s[r]:
        #         l+=1
        #         r -= 1
        #     else:
        #         r -= 1
        #         r_dif +=1
        # if r_dif <= 1:       
        #     return True
        # return False


        l = 0
        r = len(s) - 1

        while l < r:

            if s[r] != s[l] :
                strR,strL =s[l:r], s[l+1:r+1]
               
                return strR[::-1]==strR or strL[::-1]==strL
            l += 1
            r -= 1
        return True
        
        
        