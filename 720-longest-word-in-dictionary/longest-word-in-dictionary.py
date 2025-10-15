class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        dicts = set()
        print(words)
        for w in words:
            if ans == "" and len(w) == 1:
                ans = w
            if w[:len(w) - 1] in dicts  and ans[:len(ans) - 1] != w[:len(w) - 1]  and len(w) > len(ans): 
                           
                ans = w
            if len(w) == 1 or w[: len(w) - 1] in dicts:
                
                
                dicts.add(w)
        return ans
            
        