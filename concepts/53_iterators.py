# Iterators - Objects that can be iterated (looped) over

print("=" * 60)
print("ITERATORS")
print("=" * 60)

print("\n1. BASIC ITERATION")
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)
print(f"First: {next(iterator)}")
print(f"Second: {next(iterator)}")

print("\n2. ITERATE UNTIL END")
iterator = iter(my_list)
while True:
    try:
        print(next(iterator), end=" ")
    except StopIteration:
        break

print("\n\n3. CUSTOM ITERATOR CLASS")
class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1

counter = Counter(1, 5)
for num in counter:
    print(num, end=" ")

print("\n\n4. REVERSE ITERATOR")
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('Python')
print(f"Reversed: {''.join(rev)}")

print("\n5. ITERATOR VS ITERABLE")
# Iterable: can be looped over (list, tuple, string)
# Iterator: object with __iter__ and __next__
my_list = [1, 2, 3]  # Iterable
my_iter = iter(my_list)  # Iterator
print(f"List is iterable: {hasattr(my_list, '__iter__')}")
print(f"Iterator has __next__: {hasattr(my_iter, '__next__')}")
