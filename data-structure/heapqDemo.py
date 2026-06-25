import heapq

num = [5, 7, 9, 1, 3]
heapq.heapify(num)
print(num)

heapq.heappush(num, 4)
heapq.heappush(num, 10)
print(num)

heapq.heappop(num)
print(num)