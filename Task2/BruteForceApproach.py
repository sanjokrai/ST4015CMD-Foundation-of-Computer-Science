from itertools import permutations
import time

# List of students to be seated
students  = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Pairs who are friends and should NOT sit next to each other
friends   = {("Alice", "Bob"), ("Bob", "Charlie"), ("Diana", "Eve")}

# Pairs from the same city who should NOT sit next to each other
same_city = {("Alice", "Charlie"), ("Bob", "Diana")}


# Check if two students conflict (friends or same city)
def are_conflicting(a, b):
    return (a, b) in friends or (b, a) in friends or \
           (a, b) in same_city or (b, a) in same_city


# Check if the entire arrangement is valid (no adjacent conflicts)
def is_valid(arr):
    return all(not are_conflicting(arr[i], arr[i+1]) for i in range(len(arr)-1))


print("BRUTE FORCE APPROACH")
print("-" * 35)

start    = time.time()  # Start timer
attempts = 0

# Try every possible arrangement one by one
for arr in permutations(students):
    attempts += 1

    # If this arrangement has no conflicts, it is valid
    if is_valid(arr):
        elapsed = time.time() - start  # Stop timer
        print(f"Attempts : {attempts}")
        print(f"Result   : {' | '.join(arr)}")
        print(f"Time     : {elapsed:.6f} seconds")
        break  # Stop as soon as a valid arrangement is found