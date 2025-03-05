class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path + "/"
        stack = []
        path_name = ""

        for i in range(len(path)):

            if path[i] == "/":

                if path_name :
                 

                    if  stack and path_name == "..":

                        stack.pop()
                    elif path_name != ".."  and path_name != ".":              
                          
                        stack.append(path_name)
                    path_name = ""

            else:
                path_name += path[i]




        return "/" + "/".join(stack)
        