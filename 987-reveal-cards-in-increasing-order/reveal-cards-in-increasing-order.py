class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        que = deque()

        for num in sorted(deck, reverse = True):
            if que:
                que.appendleft(que.pop())
            que.appendleft(num)
        
        return list(que)
        