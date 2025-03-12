class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        nums = self.solve(numRows)  
        return nums[:len(nums) - 1] 

    def solve(self, rowIndex):

        if rowIndex == 0:

            return [[1]]

           
        else:            
            pascal = self.solve(rowIndex - 1)

            prev = pascal[-1][0]
            nums = [1]*(rowIndex + 1)

            for i in range(1,len(pascal[-1])):

                nums[i] = pascal[-1][i] + prev
                prev = pascal[-1][i]
            pascal.append(nums)
            return  pascal
        
        