class Node:
    def __init__(self, key, val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    '''
    Intuition:
    A HashMap that gets the node by its key in O(1)
    A doubly linked list that moves nodes to the most recently used position 
    When cache exceeds its capacity, removes node from the least recently used position

    Definition:
    head<->left<------------------->right<->tail
    least recently used<------>most recently used

    GET: return the value of a node given its key,
    while updating the nodes postion to most recently used
    (remove the node from current position first and add it back to the end)
    if the node doesn't exist, return -1

    PUT: remove the node from its current position, update its value, add back to the end
    if the node associated with key doesn't exist, skip the update process, 
    add its (key, value) towards dictionary and add node back to the end
    while the capacity exceeds, remove the lRU node
    '''
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.addMRU(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node=Node(key,value)
        self.cache[key]=new_node
        self.addMRU(new_node)

        if self.capacity<len(self.cache):
            node_to_remove=self.left.next
            self.remove(node_to_remove)
            del self.cache[node_to_remove.key]

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def addMRU(self,node):
        prev_node=self.right.prev
        self.right.prev=node
        prev_node.next=node
        node.next=self.right
        node.prev=prev_node