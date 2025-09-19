class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        prev = float("inf")
        ans = ""
        for word in words:
            w = set(word.lower())
            count = Counter(word.lower())
            t = True
            for i in "".join(licensePlate.split()):
              
                if i.isalpha() and  (i.lower() not in w or not count[i.lower()]):
                    print(i,word)
                    t = False
                    break
                count[i.lower()] -= 1
            
            if t and prev > len(word):
                ans  = word
                prev = len(word)
        return ans
        