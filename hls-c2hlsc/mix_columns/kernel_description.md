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