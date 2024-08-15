from typing import List

#parent at (i-1 // 2)
#child left at i * 2 + 1
#child right at i * 2 + 2
class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def heapify(self, arr) -> List[int]:
        self.heap = arr
        for i in reversed(range(0, len(self.heap) // 2)):
            self._bubble_down(i)
        
    def access(self):
        return self.heap
    
    def push(self, value) -> None:
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)
        
    def pop(self) -> int:
        if len(self.heap) == 1:
            return self.heap.pop()
        
        to_return = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return to_return
            
    
    def top(self) -> int:
        return self.heap[0] if self.heap else -1
        
    def _bubble_up(self, index):
        while index > 0 and self.heap[index] > self.heap[(index - 1) // 2]:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2
    
    def _bubble_down(self, index):
        while index * 2 + 1 < len(self.heap):
            left = index * 2 + 1
            right = index * 2 + 2
            
            if right >= len(self.heap):
                child = left
            else:
                child = left if self.heap[left] >= self.heap[right] else right
            
            if self.heap[index] < self.heap[child]:
                self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                index = child
            else:
                break

   
