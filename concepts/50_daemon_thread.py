# By default, Thread is NON-DAEMON (daemon=False)
# This means the program will wait for all non-daemon threads to complete before exiting

# Daemon Thread vs Non-Daemon Thread:
# - daemon thread: runs in background, not important for program to run
#                  program will not wait for daemon threads to complete before exiting
#                  daemon thread is killed when main program exits
# - non-daemon thread: important for program to run, keeps program alive
#                       program waits for non-daemon threads to complete before exiting

# Example: background tasks, garbage collection, waiting for input, long running processes

import threading
import time

def timer():
    """Background timer function that counts seconds logged in."""
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for: {count} seconds")

if __name__ == "__main__":
    print("Default thread behavior:")
    
    # Default: non-daemon thread (daemon=False by default)
    default_thread = threading.Thread(target=timer)
    print(f"Default daemon status: {default_thread.daemon}")  # False
    
    # Explicitly set as daemon thread
    daemon_thread = threading.Thread(target=timer, daemon=True)
    print(f"Daemon thread status: {daemon_thread.daemon}")   # True
    
    # Start daemon thread
    daemon_thread.start()
    
    # Main thread waits for user input
    answer = input("Do you wish to exit? ")
    print(f"You answered: {answer}")
    print("Program exiting - daemon thread will be terminated automatically")