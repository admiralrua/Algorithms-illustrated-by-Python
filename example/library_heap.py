# Need to solve the removeValueHeap

import sys
sys.setrecursionlimit(10000000)


def minmax_Heapify(i, heap, opt):
    here = i
    left = i * 2 + 1
    righ = i * 2 + 2
    
    if (left < len(heap)) and \
       (((opt == 'max') and (heap[left] > heap[here])) or \
        ((opt == 'min') and (heap[left] < heap[here]))):
        here = left
    
    if (righ < len(heap)) and \
       (((opt == 'max') and (heap[righ] > heap[here])) or \
        ((opt == 'min') and (heap[righ] < heap[here]))):
        here = righ
        
    if (here != i):
        heap[i], heap[here] = heap[here], heap[i]
        minmax_Heapify(here, heap, opt)
        
        
def buildHeap(n, heap, opt):
    for i in range(n//2 - 1, -1, -1):
        minmax_Heapify(i, heap, opt) 


def pushHeap(value, heap, opt):
    heap.append(value)
    i = len(heap) - 1
    
    while (i != 0) and \
          (((opt == 'max') and (heap[(i-1)//2] < heap[i])) or \
           ((opt == 'min') and (heap[(i-1)//2] > heap[i]))):
        heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
        i = (i-1)//2
        

def popHeap(heap, opt):
    length = len(heap)
    
    if (length == 0):
        return
        
    heap[0] = heap[length-1]    
    heap.pop()
    
    if len(heap) > 1:
        minmax_Heapify(0, heap, opt)   
        

def popValueHeap(value, heap, opt):
    length = len(heap)
    
    if (length == 0):
        return
        
    if (value == length-1):   
        heap.pop()
    else:        
        heap[value] = heap[length-1]
        heap.pop()
    
        if len(heap) > 1:
            minmax_Heapify(value, heap, opt)  
		
		
def removeHeap(i, heap, opt):
    here = i
    left = i * 2 + 1
    righ = i * 2 + 2
    uppe = (i-1)//2
    
    if (uppe >= 0) and \
       (((opt == 'max') and (heap[uppe] < heap[here])) or \
        ((opt == 'min') and (heap[uppe] > heap[here]))):
        here = uppe
    
    if (left < len(heap)) and \
       (((opt == 'max') and (heap[left] > heap[here])) or \
        ((opt == 'min') and (heap[left] < heap[here]))):
        here = left
    
    if (righ < len(heap)) and \
       (((opt == 'max') and (heap[righ] > heap[here])) or \
        ((opt == 'min') and (heap[righ] < heap[here]))):
        here = righ
        
    if (here != i):
        heap[i], heap[here] = heap[here], heap[i]
        minmax_Heapify(here, heap, opt)		


opt  = 'max'
tmp  = [0, 2, 4, 6, 10, 12, 1, 5, 7, 9, 11, 13]
print(tmp)

buildHeap(len(tmp), tmp, opt)
print(tmp)

pushHeap(3, tmp, opt)
pushHeap(8, tmp, opt)
print(tmp)

popHeap(tmp, opt) 
print(tmp)








    
              