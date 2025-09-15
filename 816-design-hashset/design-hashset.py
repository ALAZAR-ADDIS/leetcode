class MyHashSet:

    def __init__(self):
        self.cont = set()
        

    def add(self, key: int) -> None:
        self.cont.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.cont:
            self.cont.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.cont
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)