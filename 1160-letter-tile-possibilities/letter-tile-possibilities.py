class Solution:
    def numTilePossibilities(self, tiles: str) -> int:


        def solve():
            if not sum(count.values()):
                return 0
            ans = 0

            for c in count:

                if  count[c]:                   
                    count[c] -= 1 
                    ans += 1  + solve()
                    count[c] += 1
            return ans





        count = defaultdict(int)
        for char in tiles:
            count[char] += 1
        
        return solve()


        
      

            
