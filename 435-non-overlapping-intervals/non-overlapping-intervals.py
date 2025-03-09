class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[1])
        # intervals.sort(key = lambda x: x[0])
        minn = intervals[-1][0]
        ans =0
      

        for i in range(len(intervals)-2,-1,-1):
            if intervals[i][1] > minn: #OL
                minn = max(minn,intervals[i][0])
                ans += 1
            else:
                minn = intervals[i][0]
        return ans
        



        