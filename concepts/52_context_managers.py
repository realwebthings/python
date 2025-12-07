# Context Managers - Manage resources (files, connections) automatically

print("=" * 60)
print("CONTEXT MANAGERS (with statement)")
print("=" * 60)

print("\n1. FILE HANDLING WITHOUT CONTEXT MANAGER")
# Manual way (not recommended)
file = open('temp.txt', 'w')
file.write('Hello')
file.close()

print("\n2. FILE HANDLING WITH CONTEXT MANAGER")
# Automatic cleanup
with open('temp.txt', 'w') as file:
    file.write('Hello World')
# File automatically closed here

print("\n3. MULTIPLE CONTEXT MANAGERS")
with open('temp.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    content = input_file.read()
    output_file.write(content.upper())

print("\n4. CUSTOM CONTEXT MANAGER (Class)")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()

with FileManager('temp.txt', 'w') as f:
    f.write('Custom context manager')

print("\n5. CONTEXT MANAGER WITH DECORATOR")
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    print("Timer started")
    yield
    end = time.time()
    print(f"Timer ended: {end - start:.4f} seconds")

with timer():
    sum([i**2 for i in range(1000000)])

print("\n6. EXCEPTION HANDLING IN CONTEXT MANAGER")
@contextmanager
def error_handler():
    try:
        yield
    except Exception as e:
        print(f"Error caught: {e}")

with error_handler():
    result = 10 / 0  # This will be caught
