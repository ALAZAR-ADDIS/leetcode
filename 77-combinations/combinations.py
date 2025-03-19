class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        


        def solve(arr,ans,i = 0):
            print(len(ans),k)
            if len(ans) == k:
                stack.append(ans[::])
            
            
            for j in range(i,len(arr)):
                ans.append(arr[j])
                solve(arr,ans,i + 1)
                ans.pop()
                i =i + 1

        

        arr = [i+1 for i in range(n)]
        print(arr)
        stack = []
        solve(arr,[],0)
        
        return stack
        