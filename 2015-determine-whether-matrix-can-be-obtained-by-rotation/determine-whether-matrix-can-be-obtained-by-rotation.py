class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        #first find the transpose
      
        for i in range(4):

            for i  in range(len(mat)):
                for j in range(len(mat[0])):                

                        if i < j:
                            mat[i][j] , mat[j][i] = mat[j][i] ,mat[i][j]
           
                        
            for i in range(len(mat)):
                        mat[i] = mat[i][::-1]
            
           
                    
            if  target == mat:
                return True   
                  
        return  False


        