class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftpointer=0
        rightpointer=len(numbers)-1
        while leftpointer<=rightpointer:
            sum=numbers[leftpointer]+numbers[rightpointer]
            if sum>target:
                rightpointer-=1
            elif sum<target:
                leftpointer+=1
            else:
                return[leftpointer+1,rightpointer+1]