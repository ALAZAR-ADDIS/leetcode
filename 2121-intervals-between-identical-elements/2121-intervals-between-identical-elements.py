class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        count = {}

        for i in range(len(arr)):

            count[arr[i]]=count.get(arr[i],[])
            count[arr[i]].append(i)

        for indexes in count.values():


            total = sum(indexes)
            prifix = 0
            for i in range(len(indexes)):
                ps = i * indexes[i] - prifix
                prifix += indexes[i]
                ss = total -prifix- (len(indexes) - i -1) * indexes[i]
                arr[indexes[i]] = ss + ps

        return arr