class Solution:
    def findTheWinner(self, n: int, k: int) -> int:



        que = deque(range(1,n + 1))

        while len(que) > 1:
            i = 1
            while i < k:
                que.append(que.popleft())
                i += 1
            que.popleft()
        
        return que[-1]

        

            

        
        