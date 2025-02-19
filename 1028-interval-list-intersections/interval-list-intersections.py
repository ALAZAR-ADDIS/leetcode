class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 0
        ans = []

        while r < len(secondList) and l < len(firstList):
            start_i,end_i= firstList[l]
            start_j,end_j = secondList[r]

            start = max(start_i,start_j)
            end = min(end_i,end_j)

            if start <= end:
                ans.append([start,end])


            if end_i > end_j :
                 
                 r += 1
            else:
                 l+= 1
        return ans