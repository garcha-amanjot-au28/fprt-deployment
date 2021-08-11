# Q-2 )Write steps in heapify/percolate down method:
import sys
class MaxHeap:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.Heap = [0] * (self.maxSize + 1)
        self.Heap[0] = sys.maxsize
        self.Front = 1

    def parent (self, indexPos):
        return indexPos//2

    def leftChild(self, indexPos):
        return indexPos * 2 

    def rightChild(self, indexPos):
        return (indexPos*2) +1

    def isLeaf(self,indexPos):
        if indexPos >= (self.size//2) and indexPos <= self.size:
            return True
        return False 
    
    def swap(self, firstPos , secPos):
        self.Heap[firstPos] , self.Heap[secPos] = self.Heap[secPos] , self.Heap[firstPos]

    def maxHeapify(self , indexPos):
        if not self.isLeaf(indexPos):
            if (self.Heap[indexPos] < self.Heap[self.leftChild(indexPos)] or self.Heap[indexPos] < self.Heap[self.rightChild(indexPos)]):
                if self.Heap[self.leftChild(indexPos)] > self.Heap[self.rightChild(indexPos)]:
                    self.swap(indexPos, self.leftChild(indexPos))
                    self.maxHeapify(self.leftChild(indexPos))

                else:
                    self.swap(indexPos, self.rightChild(indexPos))
                    self.maxHeapify(self.rightChild(indexPos))

    def insert(self, element):
        if self.size >= self.maxSize:
            return 
        self.size += 1
        self.Heap[self.size] = element 
        curr = self.size
        while self.Heap[curr] > self.Heap[self.parent(curr)]:
            self.swap (curr, self.parent(curr))
            curr =  self.parent(curr)

    def Print(self):
        for i in range (1 , (self.size//2)+1):
            print (str(self.Heap[i]) +" "+str(self.Heap[2*i]) +" "+ str(self.Heap[(2*i)+1]))

    def removeMax (self):
        curr = self.Heap[self.Front]    
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -=1
        self.maxHeapify(self.Front)
        return curr 

if __name__ == '__main__':
    maxheap = MaxHeap(10)
    array = [5,3,17,10,84,19,6,22,2]
    for i in array :
        maxheap.insert(i)
    maxheap.Print()
    print()
    print(maxheap.removeMax())
    print()
    maxheap.Print()