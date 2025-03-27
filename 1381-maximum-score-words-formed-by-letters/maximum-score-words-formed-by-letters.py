class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        # def solve(i,path):
        #     nonlocal maxx

        #     if i == len(words):
        #         con = Counter(letters)
        #         temp = 0
        #         for wor in path:
        #             fre = Counter(wor)

        #             for f in fre:

        #                 if con[f] >= fre[f]:
        #                     temp += score[ord(f) - ord("a")] * fre[f]
        #                     con[f] -= fre[f]
        #                 else:
        #                     return 

        #         maxx = max(maxx,temp)
        #         return
            
        #     path.append(words[i])
        #     solve(i + 1,path)

        #     path.pop()
        #     solve(i + 1,path)

        # maxx = 0
        # solve(0,[])
     

        # return maxx
        def check(word):
            count = Counter(word)
            for  w in count:
                if main[w] < count[w]:
                    return False
            return True
        def calculate_score(word):
            scor = 0

            for w in word:
                scor += score[ord(w) - ord("a")]

            return scor

        def solve(i):
            if i == len(words):
                return 0 
            
            res = solve(i +1)

            if check(words[i]):

                for j in words[i]:
                    main[j] -= 1
                
                res = max(res, calculate_score(words[i]) + solve(i + 1))
                
                for j in words[i]:
                    main[j] += 1
                

            return res



        main = Counter(letters)
        return solve(0)


            

        