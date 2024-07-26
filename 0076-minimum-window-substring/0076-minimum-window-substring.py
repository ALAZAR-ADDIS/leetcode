class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":return ""

        window,countT={},{}
        for i in t:
            countT[i]=1+countT.get(i,0)
        
        l=0
        string=[-1,-1]
        leng=float("infinity")
        have,need=0,len(countT)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)

            if s[r] in countT and countT[s[r]]==window[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<leng:
                    leng=r-l+1
                    string=[l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                
                l+=1
        a,b=string
        return s[a:b+1] if leng!=float("infinity") else ""
