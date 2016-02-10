import Queue
class HuffmanNode(object):
    def __init__(self,left = None, right = None):
        self.left = left
        self.right = right
        #Creating the objects
    def children(self):
        return(self.left,self.right)
    def order(self,direction = None):
        if direction is None:
            direction = []
        if self.left is not None:
            if isinstance(self.left[1], HuffmanNode):
                self.left[1].order(direction+[0])
            else:
                print(self.left + direction+[0])
        if self.right is not None:
            if isinstance(self.right[1], HuffmanNode):
                self.right[1].order(direction+[0])
            else:
                print self.right + direction+[0]
freq = [
    (), 
    ]
def encode(frequencies):
    p = Queue.PriorityQueue()
    for item in frequencies:
        p.put(item)
    
    
    while p.qsize() > 1:
        left,right = p.get(),p.get()
        node = HuffmanNode (left,right)
        p.put((left[0] + right[0], node))
    return p.get()

node = encode(freq)
print(node[1].order())

    
