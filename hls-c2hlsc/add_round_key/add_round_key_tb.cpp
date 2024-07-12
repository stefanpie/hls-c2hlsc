#include <stdio.h>
#include <cstdlib>

#include "add_round_key.h"

int main() {
    srand(13); // Seed the random number generator

    state_t state;
    state_t goldenState;
    uint8_t RoundKey[176]; // AES-128 has 176 bytes of round keys for 10 rounds

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            state[i][j] = rand() % 256;
        }
    }

    for (int i = 0; i < 176; i++) {
        RoundKey[i] = rand() % 256;
    }

    // Print initial state and RoundKey
    printf("Initial state:\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%02x ", state[i][j]);
        }
        printf("\n");
    }

    printf("RoundKey (first 16 bytes):\n");
    for (int i = 0; i < 16; i++) {
        printf("%02x ", RoundKey[i]);
    }
    printf("\n");

    // Compute golden output
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            goldenState[i][j] = state[i][j];
        }
    }
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            goldenState[i][j] ^= RoundKey[(0 * Nb * 4) + (i * Nb) + j];
        }
    }

    // Run the AddRoundKey function
    AddRoundKey(0, &state, RoundKey);

    // Print the resulting state
    printf("Resulting state:\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%02x ", state[i][j]);
        }
        printf("\n");
    }

    // Print the golden state
    printf("Golden state:\n");
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%02x ", goldenState[i][j]);
        }
        printf("\n");
    }

    bool correct = true;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (state[i][j] != goldenState[i][j]) {
                correct = false;
                break;
            }
        }
    }


    if (correct) {
        printf("Test passed!\n");
        return 0;
    } else {
        printf("Test failed!\n");
        return 1;
    }
}