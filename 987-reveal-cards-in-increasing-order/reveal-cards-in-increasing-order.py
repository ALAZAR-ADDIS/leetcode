class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        # que = deque()

        # for num in sorted(deck, reverse = True):
        #     if que:
        #         que.appendleft(que.pop())
        #     que.appendleft(num)
        
        # return list(que)


        que = deque(range(len(deck)))
        ans = [0] * len(deck)
        deck.sort()

        for n in deck:
            ans[que.popleft()] = n

            if que:
                que.append(que.popleft()) 
        return ans