#pragma once

#include <stdint.h>

// state - array holding the intermediate results during decryption.
typedef uint8_t state_t[4][4];

// AES 128 parameters
#define Nb 4  // The number of columns comprising a state in AES. This is a constant in AES. Value=4
#define Nk 4  // The number of 32 bit words in a key.
#define Nr 10 // The number of rounds in AES Cipher.


void MixColumns(state_t* state);