class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0
        r = 0
        ans = []
        ON = True
        while l < len(word1) or r < len(word2)  :
            if  ON:
                if l < len(word1):
                    ans.append(word1[l])
                ON = False
                l += 1
            else:
                if r < len(word2):
                     ans.append(word2[r])
                ON = True
                r += 1
        return "".join(ans)
        