class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node=self.cache[key]
            self.remove(old_node)

        new_node=Node(key,value)
        self.cache[key]=new_node
        self.insert(new_node)

        if len(self.cache)>self.capacity:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            

    def remove(self,node):
        prev_node=node.prev
        next_node=node.next

        prev_node.next=next_node
        next_node.prev=prev_node

    def insert(self, node):
        prev_node=self.right.prev

        node.prev=prev_node
        node.next=self.right

        prev_node.next=node
        self.right.prev=node
    

