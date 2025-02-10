class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
      

        for i in range(len(strs)):
            alpha = [0]*26
            for char in strs[i]:
                    alpha[ord(char) - ord("a")] += 1

            ans[tuple(alpha)].append(strs[i])
       
        
        

        return [val  for val in ans.values()]
                    
                
        


        

        
       
            
            
        