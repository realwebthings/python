# Perfect example showing when MULTITHREADING works well
# I/O-bound tasks: file operations, network requests, database queries

import threading
import time

def download_file(url, filename):
    """Simulate downloading a file (I/O-bound task)"""
    print(f"Starting download: {filename}")
    
    # Simulate network delay with time.sleep (represents I/O wait)
    time.sleep(2)  # This simulates waiting for network response
    
    print(f"Finished download: {filename}")
    return f"Downloaded {filename}"

def read_file(filename):
    """Simulate reading a large file (I/O-bound task)"""
    print(f"Reading file: {filename}")
    
    # Simulate file I/O delay
    time.sleep(1.5)  # This simulates disk I/O wait
    
    print(f"Finished reading: {filename}")
    return f"Read {filename}"

if __name__ == "__main__":
    files_to_download = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    files_to_read = ["data1.csv", "data2.csv", "data3.csv", "data4.csv"]
    
    print("=== I/O-BOUND TASK COMPARISON ===")
    
    # 1. Sequential (single thread)
    print("\n1. Sequential execution:")
    start_time = time.time()
    
    for filename in files_to_download:
        download_file(f"http://example.com/{filename}", filename)
    
    for filename in files_to_read:
        read_file(filename)
    
    sequential_duration = time.time() - start_time
    print(f"Sequential duration: {sequential_duration:.2f} seconds")
    
    # 2. Multithreaded
    print("\n2. Multithreaded execution:")
    start_time = time.time()
    
    threads = []
    
    # Create threads for downloads
    for filename in files_to_download:
        thread = threading.Thread(target=download_file, args=(f"http://example.com/{filename}", filename))
        threads.append(thread)
    
    # Create threads for file reading
    for filename in files_to_read:
        thread = threading.Thread(target=read_file, args=(filename,))
        threads.append(thread)
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    threaded_duration = time.time() - start_time
    print(f"Multithreaded duration: {threaded_duration:.2f} seconds")
    
    # Results
    print(f"\n=== RESULTS ===")
    print(f"Sequential: {sequential_duration:.2f} seconds")
    print(f"Multithreaded: {threaded_duration:.2f} seconds")
    print(f"Speed improvement: {sequential_duration/threaded_duration:.1f}x faster!")
    
    print(f"\n=== WHY MULTITHREADING WORKS HERE ===")
    print("• I/O operations (file reading, network requests)")
    print("• GIL is RELEASED during I/O waits")
    print("• While one thread waits for I/O, others can work")
    print("• True concurrency during I/O operations")
    print("• Perfect use case for multithreading!")