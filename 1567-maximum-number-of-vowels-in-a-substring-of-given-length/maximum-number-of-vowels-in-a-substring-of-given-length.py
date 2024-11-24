class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={"a","e","i","o","u"}
        freq=0
        maxAns=0
        
        for i in range(k):
            if s[i] in vowels:
                freq+=1
        maxAns=max(maxAns,freq)
        for i in range(len(s)-k):
            if s[i] in vowels:
                freq-=1
            if s[i+k] in vowels:
                freq+=1
            maxAns=max(freq,maxAns)
        return maxAns


        