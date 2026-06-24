from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.append(10)  # Add an element to the right end
dq.appendleft(0)  # Add an element to the left end

print("Initial deque:", dq)

delItem = dq.pop()
print("Removed element:", delItem)
print(dq)  # Remove and return an element from the right end
delItem = dq.popleft()
print("Removed element:", delItem)
print(dq)  # Remove and return an element from the left end

# Insert an element at a specific position

dq.insert(0, 0) # (index, value)

print("inserted list:", dq)

dq.extend([6,3,4,5,6,7,9])

print(dq)

# write a pgm insert element into queue and check min and max value

minVal = min(dq)
maxVal = max(dq)
print(minVal)
print(maxVal)