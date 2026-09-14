class Node:
    def __init__(self, key:int, value:int):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:
    #Need a LRU cache with capacity to store doubly linked node
    #That can be accessed by its key
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    #returns node's value by its key, updates the node's position
    #to most recently used
    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    #access node's value and update if it's present in cache
    #i.e. access node->remove it->restore it
    #or create a new node and store it in the cache
    #check if capacity exceeds->pop the left most node out
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node=Node(key,value)
        self.cache[key]=node
        self.add(node)
        if len(self.cache)>self.capacity:
            node_to_remove=self.left.next 
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]

    def remove(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add(self, node):
        prev_node=self.right.prev
        prev_node.next=node
        node.prev=prev_node
        node.next=self.right
        self.right.prev=node



