class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        temp = [0,]
        left = 0
        right = 0
        maxx = float("inf")
        for num in arr:
            temp.append(abs(num - x))
        
        for i in range(1,len(temp)):
            temp[i] += temp[i - 1]
        
        l = 1
        for r in range(1,len(temp)):

            if r - l + 1 > k:
                l += 1
            print(r - l  + 1,k)
            if r - l + 1 == k and temp[r] - temp[l - 1] < maxx:
                left = l
                right = r
                maxx = temp[r] - temp[l - 1]


        return arr[left- 1: right ]
