class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        u = 0
        l = 0
        for i in range(len(word)):
            if word[i].isupper():
                u += 1
            else:
                l += 1
        if not u or not l:
            return True
        
        return u == 1 and word[0].isupper()
        
        