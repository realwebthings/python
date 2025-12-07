# Collections Module - Specialized container datatypes

from collections import Counter, defaultdict, OrderedDict, deque, namedtuple

print("=" * 60)
print("COLLECTIONS MODULE")
print("=" * 60)

print("\n1. COUNTER - Count occurrences")
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(words)
print(f"Counts: {counter}")
print(f"Most common: {counter.most_common(2)}")

print("\n2. DEFAULTDICT - Default values for missing keys")
dd = defaultdict(int)  # Default value is 0
dd['a'] += 1
dd['b'] += 2
print(f"DefaultDict: {dict(dd)}")
print(f"Missing key: {dd['c']}")  # Returns 0, not KeyError

print("\n3. ORDEREDDICT - Maintains insertion order")
# Note: Regular dicts maintain order in Python 3.7+
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"OrderedDict: {od}")

print("\n4. DEQUE - Double-ended queue (fast append/pop)")
dq = deque([1, 2, 3])
dq.append(4)        # Add to right
dq.appendleft(0)    # Add to left
print(f"Deque: {dq}")
dq.pop()            # Remove from right
dq.popleft()        # Remove from left
print(f"After pops: {dq}")

print("\n5. NAMEDTUPLE - Tuple with named fields")
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p}")
print(f"X: {p.x}, Y: {p.y}")

Person = namedtuple('Person', ['name', 'age', 'city'])
person = Person('Alice', 30, 'NYC')
print(f"Person: {person.name}, {person.age}, {person.city}")

print("\n6. COUNTER OPERATIONS")
c1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = Counter(['a', 'b', 'd'])
print(f"C1: {c1}")
print(f"C2: {c2}")
print(f"C1 + C2: {c1 + c2}")
print(f"C1 - C2: {c1 - c2}")

print("\n7. DEQUE AS STACK/QUEUE")
# Stack (LIFO)
stack = deque()
stack.append(1)
stack.append(2)
print(f"Stack pop: {stack.pop()}")

# Queue (FIFO)
queue = deque()
queue.append(1)
queue.append(2)
print(f"Queue pop: {queue.popleft()}")
