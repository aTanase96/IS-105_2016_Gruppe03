import Queue

class HuffmanNode(object):
    def __init__(self,left=None,right=None,root=None):
        self.left = left
        self.right = right
        self.root = root
    def children(self):
        return (self.left,self.right)
    def preorder(self,path=None):
        if path is None:
            path = []
        if self.left is not None:
            if isinstance(self.left[1], HuffmanNode):
                self.left[1].preorder(path+[0])
            else:
                print(self.left,path+[0])
        if self.right is not None:
            if isinstance(self.right[1], HuffmanNode):
                self.right[1].preorder(path+[1])
            else:
                print(self.right,path+[1])

freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]

def encode(frequencies):
    p = Queue.PriorityQueue()
    for item in frequencies:
        p.put(item)

    #invariant that order is ascending in the priority queue
    #p.size() gives list of elements
    while p.qsize() > 1:
        left,right = p.get(),p.get()
        node = HuffmanNode(left,right)
        p.put((left[0]+right[0],node))
    return p.get()

node = encode(freq)
print(node[1].preorder())
