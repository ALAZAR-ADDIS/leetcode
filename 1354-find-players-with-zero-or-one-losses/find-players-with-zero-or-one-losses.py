class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        part = defaultdict(int)
        win = defaultdict(int)
        ans= [[] , []]

        for match in  matches:

            part[match[0]] += 1
            part[match[1]] += 1

            win[match[0]] += 1
           
       
        
        for p in part:
         

            if  part[p] == win[p]:
                    ans[0].append(p)
            elif  part[p] - 1 == win[p]:
                    ans[1].append(p)
        ans[0].sort()
        ans[1].sort()

        return ans



[[1,2,10],[4,5,7,8]]

            
            
        
        