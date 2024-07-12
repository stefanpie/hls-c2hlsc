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