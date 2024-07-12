```
Description:
The quickSort kernel is a high-level synthesis design that implements the QuickSort algorithm, a popular sorting technique used to arrange elements of an array in ascending order. The design takes an unsorted array of integers as input and recursively partitions the array into two sub-arrays, one with elements less than a pivot element and another with elements greater than the pivot. The pivot element is then placed in its correct position, and the process is repeated for the sub-arrays until the entire array is sorted.

Top-Level Function: `quickSort`

Inputs:
- `arr`: an array of 32-bit signed integers, representing the input data to be sorted. The array is one-dimensional, and its size is variable, but it is assumed to be a power of 2.
- `low`: a 32-bit signed integer, representing the starting index of the sub-array to be sorted.
- `high`: a 32-bit signed integer, representing the ending index of the sub-array to be sorted.

Outputs:
- `arr`: the sorted array of 32-bit signed integers, with the same size and layout as the input array.

Important Data Structures and Data Types:
- `int`: a 32-bit signed integer data type, used to represent the elements of the input array and the indices.
- `int[]`: a one-dimensional array of 32-bit signed integers, used to represent the input data and the partitioned sub-arrays.

Sub-Components:
- `swap`: a function that swaps two elements of the input array, used to exchange elements during the partitioning process.
- `partition`: a function that partitions the input array into two sub-arrays based on a pivot element, used to recursively sort the array.
```