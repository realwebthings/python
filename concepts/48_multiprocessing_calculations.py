#cpu bound = program/task spends most of it's time doing calculations (data analysis, image processing, encryption/decryption, mathematical computations)
#io bound = program/task spends most of it's time waiting for external events (user input, web scraping, file reading/writing, network requests)

# thread =  flow of execution like a separate order of instructions.
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock),
#           allows only one thread to hold the control of the Python interpreter.

# cpu bound = program/task spends most of it's time doing calculations (internal events : cpu externsive)
#              use multiprocessing (bypasses GIL)

# io bound = program/task spends most of it's time waiting for external events
#            use multithreading (GIL released during I/O operations)


# === WHAT IS GIL? ===
# GIL = Global Interpreter Lock
# • A mutex that prevents multiple threads from executing Python code simultaneously
# • Only ONE thread can execute Python bytecode at a time
# • Protects Python's memory management (reference counting)
# • Makes Python thread-safe but limits true parallelism

# === GIL Impact ===
# CPU-bound tasks:
# • Multiple threads DON'T help (they take turns)
# • Use multiprocessing instead (separate processes = separate GILs)

# I/O-bound tasks:
# • GIL is RELEASED during I/O operations (file read, network calls)
# • Other threads can run while one thread waits for I/O
# • Multithreading IS beneficial here

# === Simple Analogy ===
# GIL is like a single bathroom key in an office:
# • Only one person can use the bathroom at a time
# • Others must wait their turn
# • But while someone is waiting for delivery (I/O), they give up the key


import threading
import time
def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]
    print(numbers)

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time

    print(f"Duration {duration} seconds")


# === NUMERIC LITERALS WITH UNDERSCORES ===
# Python allows underscores in numbers for better readability
# 5_000_000 = 5000000 (five million)
# The underscores are ignored by Python - they're just for humans

    print("Examples:")
    print(f"5_000_000 = {5_000_000}")
    print(f"1_000 = {1_000}")
    print(f"1_234_567 = {1_234_567}")

# So your numbers list creates:
# [5000000, 5000001, 5000002, 5000003, ..., 5000019]
# These are large numbers to make the CPU work hard for demonstration
# === WHY DOES IT TAKE 3+ SECONDS? ===
# Let's break down what's happening:

# 1. You have 20 numbers: [5000000, 5000001, 5000002, ..., 5000019]
# 2. For EACH number, cpu_bound() calculates: sum(i * i for i in range(number))
# 3. This means for 5,000,000 it calculates: 0² + 1² + 2² + 3² + ... + 4,999,999²

# Example of the workload:
# - First number (5,000,000): calculates 5 million squares and sums them
# - Second number (5,000,001): calculates 5,000,001 squares and sums them
# - And so on for all 20 numbers...

# Total operations: roughly 20 × 5,000,000 = 100,000,000 calculations!
# That's why it takes several seconds - your CPU is working very hard

    print("\nWorkload breakdown:")
    print("Numbers to process:", len(numbers))
    print("Operations per number: ~5,000,000")
    print("Total operations: ~100,000,000")
    print("This is intentionally CPU-intensive to demonstrate threading concepts")






    print("===============****************=============")
    print("\nThreading examples")

    print("1. Single thread")
    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")

    print("\n2. Multiple threads")
    start_time = time.time()  # Reset timer for threading test
    thread1 = threading.Thread(target=find_sums, args=(numbers,))
    thread2 = threading.Thread(target=find_sums, args=(numbers, ))
    print("Active Threads: ", threading.active_count())
    print("Enumerate: ", threading.enumerate())
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    
    print("\n=== WHY THREADING IS SLOWER FOR CPU-BOUND TASKS ===")
    print("• GIL allows only ONE thread to execute Python code at a time")
    print("• Threads take turns running (context switching overhead)")
    print("• Two threads doing the SAME work = 2x the total work")
    print("• Plus thread management overhead makes it even slower")
    print("• For CPU-bound tasks, use MULTIPROCESSING instead!")

    
    print("\n3. Multiprocessing (splits work across processes)")
    import multiprocessing
    print(multiprocessing.cpu_count())
    # Split the work between processes
    half = len(numbers) // 2
    numbers1 = numbers[:half]  # First half: [5000000, 5000001, ..., 5000009]
    numbers2 = numbers[half:]  # Second half: [5000010, 5000011, ..., 5000019]
    
    start_time = time.time()
    process1 = multiprocessing.Process(target=find_sums, args=(numbers1,))
    process2 = multiprocessing.Process(target=find_sums, args=(numbers2,))
    
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    
    print("\n=== WHY MULTIPROCESSING IS FASTER ===")
    print("• Each process has its own GIL (bypasses the limitation)")
    print("• True parallelism: both processes run simultaneously")
    print("• Work is SPLIT between processes (not duplicated)")
    print("• Each process handles 10 numbers instead of 20")
    print("• Should be roughly 2x faster than single thread!")

    print("\n=== MULTIPROCESSING POOL ===")
    print("\n4. Multithreading with SPLIT work (still limited by GIL)")
    # Split work between threads (like we did with multiprocessing)
    half = len(numbers) // 2
    numbers1 = numbers[:half]  # First half
    numbers2 = numbers[half:]  # Second half
    
    start_time = time.time()
    thread1 = threading.Thread(target=find_sums, args=(numbers1,))
    thread2 = threading.Thread(target=find_sums, args=(numbers2,))
    
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    
    print("\n=== WHY THREADING STILL CAN'T BEAT MULTIPROCESSING ===")
    print("• Even with split work, threads still take turns due to GIL")
    print("• Only ONE thread can execute Python code at any moment")
    print("• No true parallelism - threads switch back and forth")
    print("• Context switching adds overhead")
    print("• Will be slower than multiprocessing but faster than duplicate work")
    
    print("\n=== WHEN TO USE MULTITHREADING ===")
    print("• I/O-bound tasks (file reading, network requests, database queries)")
    print("• Tasks that wait for external resources")
    print("• GIL is released during I/O operations")
    print("• Example: downloading multiple files simultaneously")