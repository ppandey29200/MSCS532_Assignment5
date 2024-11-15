# MSCS532_Assignment5

This repository contains implementations of both deterministic and randomized versions of the Quicksort algorithm. Additionally, it includes a test class to generate different test cases (best case, average case, and worst case) and measure the execution time of each sorting algorithm.

## Files

- `differentQuicksorts.py`: Contains the implementations of deterministic and randomized Quicksort algorithms, as well as the test class to run and measure the performance of these algorithms.

## Requirements

- Python 3.x
- `time` module (standard library)
- `random` module (standard library)

## How to Run the Code

### Windows

1. Open Command Prompt.
2. Navigate to the directory containing `differentQuicksorts.py`:
   cd path\to\your\directory
3. Run the script:
    python differentQuicksorts.py

### Mac and Linux
1. Open Terminal.
2. Navigate to the directory containing differentQuicksorts.py:
    cd /path/to/your/directory
3. Run the script:
    python3 differentQuicksorts.py


## What the Code Does
### Deterministic Quicksort
The deterministic Quicksort implementation selects the last element of the array as the pivot. It partitions the array into three lists: elements smaller than the pivot, elements equal to the pivot, and elements larger than the pivot. It then recursively sorts the smaller and larger partitions and concatenates the results.

### Randomized Quicksort
The randomized Quicksort implementation selects a random element of the array as the pivot. Similar to the deterministic version, it partitions the array into three lists: elements smaller than the pivot, elements equal to the pivot, and elements larger than the pivot. It then recursively sorts the smaller and larger partitions and concatenates the results.

### Test Class
The TestQuicksort class generates different test cases (best case, average case, and worst case) and measures the execution time of each sorting algorithm. It includes methods to generate the test cases and measure the execution time of the sorting functions.

### Example Output
When you run the script, it will generate and sort the test cases using both deterministic and randomized Quicksort algorithms. It will print the execution time for each test case and sorting algorithm.<br>
=== Testing Deterministic Quicksort ===<br>
Best Case Execution Time: 0.001234 seconds<br>
Average Case Execution Time: 0.002345 seconds<br>
Worst Case Execution Time: 0.003456 seconds<br>

=== Testing Randomized Quicksort ===<br>
Best Case Execution Time: 0.001234 seconds<br>
Average Case Execution Time: 0.002345 seconds<br>
Worst Case Execution Time: 0.003456 seconds<br>

Adjust the sizes variable in the script to change the size of the test cases.