class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp,value])
        # self.map[key].sort(key = lambda x: x[0])
        
        

    def get(self, key: str, timestamp: int) -> str:
        
        l = -1
        r = len(self.map[key])

        while l + 1 < r:
            mid = (l + r)//2
            if self.map[key][mid][0] <= timestamp:
                l = mid
            else:
                r = mid
        return self.map[key][l][1] if l >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)