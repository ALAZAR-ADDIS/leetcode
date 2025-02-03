class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        # check_range = {i for i in range(left,right+1)}

        # existing_range = set()

        # for _range in ranges:

        #     existing_range.update({i for i in range(_range[0],_range[1]+1)})

        
        # for i in check_range:

        #     if i not in existing_range:
        #         return False

        # return True
        
        ranges_covered = [0]*52

        for _range in ranges:

            ranges_covered[_range[0]] += 1
            ranges_covered[_range[-1]+1] -= 1

        for i in range(1,52):
            ranges_covered[i] += ranges_covered[i-1]

        
        for i in range(left,right+1):

            if ranges_covered[i] == 0:
                return False

        return True