class TreeNode():
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.child[ord(char) - ord("a")]:
                curr.child[ord(char) - ord("a")] = TreeNode()
            curr = curr.child[ord(char) - ord("a")]
        
        curr.is_end = True
       
        

    def search(self, word: str) -> bool:
      

        def solve(i,curr):
              
            if i == len(word): 
                
                return curr.is_end


            if word[i] == ".":
                for n  in curr.child:
                    if n :                    
                        if  solve(i + 1, n):
                            return True
            elif curr.child[ord(word[i]) - ord("a")]:
                        if  solve(i + 1,curr.child[ord(word[i]) - ord("a")] ):                      
                            return True
            
            return False
        return solve(0, self.root)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)