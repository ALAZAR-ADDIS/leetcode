class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []

        for i in range(len(logs)):

            if logs[i] == "../" or  logs[i] == "./":
                if stack and logs[i] == "../":
                    stack.pop()
                continue
            stack.append(logs[i])
        return len(stack)
        