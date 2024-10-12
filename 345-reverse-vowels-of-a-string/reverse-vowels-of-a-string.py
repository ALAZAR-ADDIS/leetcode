class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r=0,len(s)-1
        s=[i for i in s]
        v=['a', 'e', 'i', 'o',"u"]

        while r>=l:
            if s[l].lower() in v  and s[r].lower() in v:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[r].lower() in v:
                l+=1
            else:
                r-=1
        return "".join(s)

        