class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        def solve(i,path):
            if i == len(word):
                if path:                
                    ans.append("".join(path))
                return 
            
            temp = word[i]
            for w in temp:
                path.append(w)
                solve(i + 1,path)
                path.pop()
            

        maped = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs", "8":"tuv","9":"wxyz"}

        word = []
        for  d in digits:
            word.append(maped[d])         
          
        ans = []
        solve(0,[])
        return ans
            
            