# Kernel Descriptions

## add_round_key

An implementation of the "add round key" step of the AES encryption algorithm. It is responsible for adding the round key to the state in each round of the encryption process. The round key is added to the state by performing an XOR operation between the state and the round key. This kernel is designed to be highly efficient and optimized for hardware implementation.

Top-Level Function: `AddRoundKey`

Inputs:

- `round`: an 8-bit unsigned integer representing the current round number.
- `state`: a 2D array of 4x4 unsigned 8-bit integers, representing the intermediate state of the encryption process.
- `RoundKey`: a 1D array of unsigned 8-bit integers, representing the round key for the current round.

Outputs:

- `state`: the updated 2D array of 4x4 unsigned 8-bit integers, representing the state after adding the round key.

Important Data Structures and Data Types:

- `state_t`: a 2D array of 4x4 unsigned 8-bit integers, representing the intermediate state of the encryption process.
- `uint8_t`: an 8-bit unsigned integer type, used to represent individual bytes of the state and round key.

Sub-Components:

- None. The AddRoundKey kernel is a self-contained function that performs the round key addition operation.

## mix_columns

An implementation of the "mix columns" step of the AES decryption process. It performs a linear transformation on the columns of the state matrix, which is a 4x4 array of bytes. The kernel takes the state matrix as input and applies a series of bitwise XOR and shift operations to mix the columns, ensuring that each byte of the output depends on all bytes of the input. This mixing process is a crucial step in the AES decryption algorithm, as it provides diffusion and confusion, making it difficult for attackers to deduce the encryption key.

Top-Level Function: `MixColumns`

Inputs:

- `state`: a 4x4 array of bytes (uint8_t) representing the intermediate results during decryption.

Outputs:

- `state`: the modified 4x4 array of bytes (uint8_t) after applying the MixColumns transformation.

Important Data Structures and Data Types:

- `state_t`: a 4x4 array of bytes (uint8_t) representing the state matrix, which is the intermediate result during decryption.

Sub-Components:

- `xtime`: a helper function that performs a bitwise left shift and conditional XOR operation on a single byte, used to compute the mixed columns.

## shift_rows

An implementation of the "shift rows" step of the AES decryption process. It performs a row-wise shifting operation on the intermediate state matrix, where each row is shifted to the left by a different offset. The offset for each row is equal to the row number, starting from 0. This operation is a key step in the AES decryption algorithm, ensuring that the data is properly transformed and aligned for subsequent processing.

Top-Level Function: `ShiftRows`

Inputs:

- `state`: a 2D array of 4x4 uint8_t elements, representing the intermediate state matrix in the AES decryption process.

Outputs:

- `state`: the modified 2D array of 4x4 uint8_t elements, where each row has been shifted to the left by a different offset.

Important Data Structures and Data Types:

- `state_t`: a 2D array of 4x4 uint8_t elements, representing the intermediate state matrix in the AES decryption process. This data structure is used to store and manipulate the data during the decryption process.

Sub-Components:

- None. The ShiftRows kernel is a self-contained function that performs the row-wise shifting operation without relying on any external sub-components.

## sub_bytes

An implementation of the "sub bytes" step of the AES decryption process. It takes a 4x4 state matrix as input and substitutes each byte of the matrix with a corresponding value from a pre-computed S-box lookup table. The S-box is a non-linear substitution table that is used to introduce confusion in the AES algorithm. The kernel iterates over each byte of the input state matrix, performs a table lookup using the S-box, and replaces the original byte with the substituted value.

Top-Level Function: `SubBytes`

Inputs:

- `state`: a 4x4 matrix of uint8_t values, representing the intermediate results during decryption.

Outputs:

- `state`: the modified 4x4 matrix of uint8_t values, with each byte substituted using the S-box lookup table.

Important Data Structures and Data Types:

- `state_t`: a 4x4 matrix of uint8_t values, used to represent the intermediate results during decryption.
- `sbox`: a 256-element lookup table of uint8_t values, used for substitution.

Sub-Components:

- `getSBoxValue`: a function that performs a table lookup using the S-box and returns the substituted value for a given input byte.

## quicksort

An implementation of the QuickSort algorithm, a popular sorting technique used to arrange elements of an array in ascending order. The design takes an unsorted array of integers as input and recursively partitions the array into two sub-arrays, one with elements less than a pivot element and another with elements greater than the pivot. The pivot element is then placed in its correct position, and the process is repeated for the sub-arrays until the entire array is sorted.

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