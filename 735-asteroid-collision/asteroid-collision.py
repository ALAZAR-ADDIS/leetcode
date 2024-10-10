class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # traverce out through the list
        #astroids[i]<0
        #while stack and stack[-1]<abs(a[i])
        stack=[]

        for i in range(len(asteroids)):
                
                while  stack and (stack[-1]>0>asteroids[i]):
                    
                    if stack[-1]<abs(asteroids[i]):
                       stack.pop()
                    elif stack[-1]==abs(asteroids[i]):
                        stack.pop()
                        break
                    else: break
                else:
                    stack.append(asteroids[i])
               
                
                        
            
      
        return stack

        