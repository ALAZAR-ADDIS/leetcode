class TreeNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.count = 0


class Solution:
    def __init__(self):
        self.root = TreeNode()
    def insert(self,word):
        curr = self.root
        for char in word:
            if not curr.child[ord(char) - ord("a")]:
                curr.child[ord(char) - ord("a")] = TreeNode()
            curr = curr.child[ord(char) - ord("a")]
            curr.count += 1
            
        
        

    def sumPrefixScores(self, words: List[str]) -> List[int]:

        def solve(curr,word):
            ans = 0
            for char in word:                
                if  curr.child[ord(char) - ord("a")]:
                                       
                    curr = curr.child[ord(char) - ord("a")]
                   
                    ans +=  curr.count
                   
            return ans 

        for w in words:
            self.insert(w)
        solve(self.root,"abc")
        ans = []
        for w in words:
            ans.append(solve(self.root,w))
        
        return ans

            
        