class TreeNode():
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if not curr.child[ord(char) - ord("a")]:
                curr.child[ord(char) - ord("a")] = TreeNode()
            
            curr = curr.child[ord(char) - ord("a")] 
        
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if not curr.child[ord(char) - ord("a")] :
                return False
            curr = curr.child[ord(char) - ord("a")]
        
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if not curr.child[ord(char) - ord("a")] :
                return False
            curr = curr.child[ord(char) - ord("a")]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)