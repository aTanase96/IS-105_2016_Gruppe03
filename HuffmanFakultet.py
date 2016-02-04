import queue
class huffman(object):
    def __init__(self,left = None, right = None):
        self.left = left
        self.right = right
    def children(self):
        return(self.left,self.right)
    def order(self,direction = None):
        if direction is None:
            direction = []
        if self.left is not None:
            if isinstance(self.left[1], huffman):
                self.left[1].order(direction + [0])
            else:
                print(self.left + direction + [0])
    