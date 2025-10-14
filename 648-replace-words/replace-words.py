class TreeNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TreeNode()
    def create(self, word):
        curr = self.root
        for char in word:
            if not curr.child[ord(char) - ord("a")]:
                curr.child[ord(char) - ord("a")] = TreeNode()
            curr = curr.child[ord(char) - ord("a")]
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for index,char in enumerate(word):
            if curr.is_end:
                return index
            if not curr.child[ord(char) - ord("a")]:
                return -1
            curr = curr.child[ord(char) - ord("a")]
        
        return len(word)
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        for w in dictionary:
            self.create(w)
        
        words = sentence.split()

        ans = []
        for w in words:
            index = self.search(w)
            print(w)
            if index > -1:

                ans.append( w[: index ])
            else:
                ans.append( w[:  ])

        
        return " ".join(ans)
         



        
        