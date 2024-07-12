#include <stdio.h>
#include <cstdlib>

#include "mix_columns.h"

// Function to print the state for debugging
void print_state(const state_t state) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%02x ", state[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

// Function to generate random state
void generate_random_state(state_t state) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            state[i][j] = rand() % 256;
        }
    }
}

// Function to copy state
void copy_state(state_t dest, const state_t src) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            dest[i][j] = src[i][j];
        }
    }
}

// Function to compare two states
int compare_states(const state_t state1, const state_t state2) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (state1[i][j] != state2[i][j]) {
                return 0; // States are different
            }
        }
    }
    return 1; // States are the same
}



int main() {
    srand(13); // Seed the random number generator

    state_t state, golden_state;

    // Generate random input state
    generate_random_state(state);

    // Copy the state to golden_state
    copy_state(golden_state, state);

    // Apply the MixColumns function
    MixColumns(&state);

    // Apply the golden MixColumns function
    // Alternative MixColumns implementation for golden computation
    
    {
        #define xtime(x) ((x << 1) ^ (((x >> 7) & 1) * 0x1b))

        uint8_t i;
        uint8_t a, b, c, d;
        for (i = 0; i < 4; ++i) {
            a = golden_state[i][0];
            b = golden_state[i][1];
            c = golden_state[i][2];
            d = golden_state[i][3];

            golden_state[i][0] = xtime(a) ^ xtime(b) ^ b ^ c ^ d;
            golden_state[i][1] = a ^ xtime(b) ^ xtime(c) ^ c ^ d;
            golden_state[i][2] = a ^ b ^ xtime(c) ^ xtime(d) ^ d;
            golden_state[i][3] = xtime(a) ^ a ^ b ^ c ^ xtime(d);
        }
    }

    // Print the original, modified, and golden states
    printf("Original State:\n");
    print_state(state);
    printf("Modified State:\n");
    print_state(state);
    printf("Golden State:\n");
    print_state(golden_state);

    // Compare the result
    if (compare_states(state, golden_state)) {
        printf("Test passed: The MixColumns function output matches the golden output.\n");
        return 0;
    } else {
        printf("Test failed: The MixColumns function output does not match the golden output.\n");
        return 1;
    }
}