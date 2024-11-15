import random
import time
import sys

# Increase the recursion limit
sys.setrecursionlimit(6000)  # Adjust this value as needed

# Deterministic Quicksort Implementation
def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    pivot = arr[-1]  # Select the last element as the pivot
    smaller, equal, larger = [], [], []
    
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    
    return deterministic_quicksort(smaller) + equal + deterministic_quicksort(larger)

# Randomized Quicksort Implementation
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    smaller, equal, larger = [], [], []
    
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    
    return randomized_quicksort(smaller) + equal + randomized_quicksort(larger)

# Function to generate test cases
def generate_test_case(n, case_type="random"):
    if case_type == "random":
        return [random.randint(0, 1000) for _ in range(n)]  # Random case
    elif case_type == "sorted":
        return list(range(n))  # Sorted case
    elif case_type == "reverse_sorted":
        return list(range(n, 0, -1))  # Reverse sorted case

# Function to measure execution time
def measure_execution_time(sort_function, arr):
    start_time = time.time()
    sorted_arr = sort_function(arr)
    end_time = time.time()
    return sorted_arr, end_time - start_time

# Test with different cases
sizes = [100, 1000, 5000]  # Different sizes for performance testing

for size in sizes:
    # Generate test cases
    random_case = generate_test_case(size, "random")
    sorted_case = generate_test_case(size, "sorted")
    reverse_sorted_case = generate_test_case(size, "reverse_sorted")

    # Test deterministic Quicksort
    print(f"=== Testing Deterministic Quicksort (Size {size}) ===")
    
    # Best Case: Sorted
    sorted_array, time_taken = measure_execution_time(deterministic_quicksort, sorted_case)
    print(f"Best Case (Sorted) - Original Array: {sorted_case[:10]}... Sorted Array: {sorted_array[:10]}... Time: {time_taken:.6f} seconds")
    
    # Average Case: Random
    random_array, time_taken = measure_execution_time(deterministic_quicksort, random_case)
    print(f"Average Case (Random) - Original Array: {random_case[:10]}... Sorted Array: {random_array[:10]}... Time: {time_taken:.6f} seconds")
    
    # Worst Case: Reverse Sorted
    reverse_sorted_array, time_taken = measure_execution_time(deterministic_quicksort, reverse_sorted_case)
    print(f"Worst Case (Reverse Sorted) - Original Array: {reverse_sorted_case[:10]}... Sorted Array: {reverse_sorted_array[:10]}... Time: {time_taken:.6f} seconds")
    
    # Test randomized Quicksort
    print(f"=== Testing Randomized Quicksort (Size {size}) ===")
    
    # Best Case: Sorted
    sorted_array, time_taken = measure_execution_time(randomized_quicksort, sorted_case)
    print(f"Best Case (Sorted) - Original Array: {sorted_case[:10]}... Sorted Array: {sorted_array[:10]}... Time: {time_taken:.6f} seconds")
    
    # Average Case: Random
    random_array, time_taken = measure_execution_time(randomized_quicksort, random_case)
    print(f"Average Case (Random) - Original Array: {random_case[:10]}... Sorted Array: {random_array[:10]}... Time: {time_taken:.6f} seconds")
    
    # Worst Case: Reverse Sorted
    reverse_sorted_array, time_taken = measure_execution_time(randomized_quicksort, reverse_sorted_case)
    print(f"Worst Case (Reverse Sorted) - Original Array: {reverse_sorted_case[:10]}... Sorted Array: {reverse_sorted_array[:10]}... Time: {time_taken:.6f} seconds")
    
    print("="*50)
