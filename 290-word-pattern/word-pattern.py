class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        mapP={}
        mapS={}
        
        if len(words)!=len(pattern):
            return False
        
        for i in range(len(words)):
            
            if (words[i] in mapS and mapS[words[i]]!=pattern[i]) or (pattern[i] in mapP  and mapP[pattern[i]]!=words[i]):
                return False
        
            mapS[words[i]]=pattern[i]
            mapP[pattern[i]]=words[i]
        
        return True
        