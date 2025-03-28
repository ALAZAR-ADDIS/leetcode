class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # def helper(path):
        #     nonlocal maxx
        #     spath = set(path)
        #     for j in path:
        #         if not(j.upper() in spath and j.lower() in spath):

        #             return 
        #     if len(path) > len(maxx):
        #             maxx = "".join(path)

        # def solve(path,i):
        #     if path:
        #          helper(path)
            

           

        #     if i == len(s):               
        #         return 
            
        #     for j in range(i+1 , len(s)):
        #         path.append(s[i])
        #         solve(path, i + 1)
        #         path.pop()
        # maxx = ""
        # solve([],0)
        # return maxx
        
        def solve(data):
            if not data:
                return "" 
            
            cases = set(data)

            for i,n in enumerate(data):
                swaped = n.swapcase()
                if swaped not in cases:
                    left = solve(data[:i])
                    right = solve(data[i + 1:])

                    if len(left) >= len(right):
                        return left
                    return right
            return data
        return solve(s)
