class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        def mergSort(piles, left, right):

            if left < right:
                mid = (left + right) // 2
                mergSort(piles, left, mid)
                mergSort(piles, mid + 1, right)
                merg(piles, left, mid, right)

        def merg(piles, left, mid, right):
            lm, rm = left, mid + 1
            temp = []
            while lm <= mid and rm <= right:
                if piles[lm] < piles[rm]:
                    temp.append(piles[lm])
                    lm += 1
                else:
                    temp.append(piles[rm])
                    rm += 1
            while lm <= mid:
                temp.append(piles[lm])
                lm += 1
            while rm <= right:
                temp.append(piles[rm])
                rm += 1
            for i in range(left, right+1):
                piles[i] = temp[i - left]

        mergSort(piles,0,len(piles)-1)
        max=0
        count=-2
        for i in range(0,len(piles)//3):
            max+=piles[count]
            count+=-2
            
        return max


