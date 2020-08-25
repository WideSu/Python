#useful methods:
heap = [] #create an array to represent heap
heapq.heappush(heap, item) #push a new element
item = heapq.heappop(heap) #pop the smallest item
item = heap[0] #find the smallest item but does not pop it
heapq.heapify(array) #transform list into a heap, in-place
item = heapq.heapreplace(heap,value) #pop the smallest one and then push new item

'''
example:
heap = []
heapq.heappush(heap,(-1,2))
heapq.heappush(heap,(1,3))
print(heap) #[(-1,2),(1,3)]
heapq.heappush(heap,(-5,6))
print(heap) #[(-5,6),(1,3),(-1,2)]

print(heapq.heappop(heap)) #(-5,6)
print(heap) #[(-1,2),(1,3)]

heap = [6,4,5]
heapq.heapify(heap) #[4,6,5]
'''
