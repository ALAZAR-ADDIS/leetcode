class Node:
    def __init__(self,key,val,next=None,prev=None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev


class LRUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.map={}
        self.l,self.r=Node(key=0,val=0),Node(0,0)
        self.l.next,self.r.prev=self.r,self.l
        
        
        

    def get(self, key: int) -> int:
        if key in self.map:
            self.delete(self.map[key]) 
            self.insert(self.map[key])
            return self.map[key].val
        return -1
        
                
            

        
    def insert(self,node):
        self.r.prev.next=node
        node.next=self.r
        node.prev=self.r.prev
        self.r.prev=node
        
    def delete(self,node):
        print(node)
        node.prev.next=node.next
        node.next.prev=node.prev
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val=value
            self.delete(self.map[key]) 
            self.insert(self.map[key])           
        else:
            newNode=Node(key,value)
            
            self.insert(newNode)
            self.map[key]=newNode

            if len(self.map)>self.size:                
                self.map.pop(self.l.next.key)
                self.delete(self.l.next)
                

           
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)