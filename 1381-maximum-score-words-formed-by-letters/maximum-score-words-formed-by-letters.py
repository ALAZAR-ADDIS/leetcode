class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def solve(i,path):
            nonlocal maxx

            if i == len(words):
                con = Counter(letters)
                temp = 0
                for wor in path:
                    fre = Counter(wor)

                    for f in fre:

                        if con[f] >= fre[f]:
                            temp += score[ord(f) - ord("a")] * fre[f]
                            con[f] -= fre[f]
                        else:
                            return 

                maxx = max(maxx,temp)
                return
            
            path.append(words[i])
            solve(i + 1,path)

            path.pop()
            solve(i + 1,path)

        maxx = 0
        solve(0,[])
     

        return maxx
            

        