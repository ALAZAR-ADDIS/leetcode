class TreeNode:
    def __init__(self):
        self.child = [None for _ in range(26)]
        self.value = 0

class MapSum:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for  char in key:
            if not curr.child[ord(char) - ord("a")]:
                 curr.child[ord(char) - ord("a")] = TreeNode()
            curr =  curr.child[ord(char) - ord("a")]
           
        curr.value = val

        

    def sum(self, prefix: str) -> int:
        def solve(curr):
            ans = 0
            for pos in curr.child:
                if pos:
                    ans += solve(pos) + pos.value
                
            return ans

        curr = self.root
        ans = 0
        for char in prefix:
            if  not curr.child[ord(char) - ord("a")]:
                return 0
            curr =  curr.child[ord(char) - ord("a")]
        
        ans += solve(curr) + curr.value

        return ans

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)