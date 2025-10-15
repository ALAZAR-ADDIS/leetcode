class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        dicts = set()
        dicts.add("")
        
        # for w in words:
        #     if ans == "" and len(w) == 1:
        #         ans = w

        #     if w[:len(w) - 1] in dicts  and ans[:len(ans) - 1] != w[:len(w) - 1]  and len(w) > len(ans):                           
        #         ans = w
        #     if len(w) == 1 or w[: len(w) - 1] in dicts:
                
                
        #         dicts.add(w)

        for word in words:
            if word[:-1] in dicts:
                dicts.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans
            
        