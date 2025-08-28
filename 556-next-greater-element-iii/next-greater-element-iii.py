class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = []

        rem = n % 10
        n = n // 10
        stack.append(rem)

        found = 0
        while n > 0:
            curr = n % 10
            n = n // 10

            if curr < rem:
                stack.append(curr)
                found = 1
                break
            
            stack.append(curr)
            rem = curr
            
        print(found)
        if not found:
            return -1
        for i in range(len(stack)):
            if stack[i] > stack[-1]:
                stack[i], stack[-1] = stack[-1], stack[i]
                break
        val = stack.pop()
        stack.sort()
        n = n * 10 + val

        for i in stack:
            n = n * 10 + i
       
        print(n)
        return n if n <= (2 ** 31) - 1 else -1





        

        
        