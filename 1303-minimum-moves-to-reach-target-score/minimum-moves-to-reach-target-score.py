class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        curr = target
        move = 0

        while curr > 1:

            if maxDoubles:             
                move += 1
                maxDoubles -= 1

                move +=1 if (curr//2)*2 != curr else 0

                curr = curr // 2
              
            else:
              move += curr - 1
              break

        return move



        