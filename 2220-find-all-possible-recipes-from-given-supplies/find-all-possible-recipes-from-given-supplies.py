class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # set the supply to infinity
        # iterate over the ingredient and add 1 if not supply
        supply = set(supplies)
        rec = set(recipes)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(recipes)):
            for ing  in  ingredients[i]:

                graph[ing].append(recipes[i])
                if ing not in supply:                    
                    indegree[recipes[i]] += 1
                else:
                    indegree[ing] = float("inf")
        qu = deque()
        for r in recipes:
            if not indegree[r]:
                qu.append(r)

        ans = []
        while qu:
            

            for _ in range(len(qu)):
                node = qu.popleft()
                ans.append(node)

                for n in graph[node]:
                    indegree[n] -= 1

                    if not indegree[n]:
                        qu.append(n)
        return ans
        
        


        