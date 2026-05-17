#include <stdio.h>

int main() {
    volatile unsigned char slol[4] = {0x5e, 0x62, 0xe0, 0x00}; 
    for (volatile int i = 0; i < 30; i++) {
        switch (i) {
            case 0: slol[1] = slol[1] ^ slol[2]; slol[2] = slol[1] ^ slol[2]; slol[1] = slol[1] ^ slol[2]; slol[2] = (slol[2] + 151) & 0xff; slol[2] = (slol[2] - 117) & 0xff; slol[0] = (slol[0] + 183) & 0xff; break;
            case 1: slol[0] = (slol[0] * 0xff) & 0xff; slol[2] ^= 136; slol[0] = (slol[0] - 63) & 0xff; slol[1] = (slol[1] - 146) & 0xff; break;
            case 2: slol[0] = (slol[0] - 235) & 0xff; slol[1] = slol[1] ^ slol[0]; slol[0] = slol[1] ^ slol[0]; slol[1] = slol[1] ^ slol[0]; slol[2] = (slol[2] - 158) & 0xff; slol[1] = (slol[1] * 0xa1) & 0xff; break;
            case 3: slol[2] = (slol[2] + 176) & 0xff; slol[1] ^= 249; slol[0] = (slol[0] + 42) & 0xff; slol[0] = slol[0] ^ slol[2]; slol[2] = slol[0] ^ slol[2]; slol[0] = slol[0] ^ slol[2]; break;
            case 4: slol[2] = (slol[2] + 148) & 0xff; slol[0] = (slol[0] + 26) & 0xff; slol[0] = slol[0] ^ slol[1]; slol[1] = slol[0] ^ slol[1]; slol[0] = slol[0] ^ slol[1]; slol[1] = (slol[1] * 0x39) & 0xff; break;
            case 5: slol[2] = slol[2] ^ slol[1]; slol[1] = slol[2] ^ slol[1]; slol[2] = slol[2] ^ slol[1]; slol[0] ^= 230; slol[0] = (slol[0] - 220) & 0xff; slol[2] ^= 74; break;
            case 6: slol[2] ^= 239; slol[0] = (slol[0] * 0x03) & 0xff; slol[1] = (slol[1] + 102) & 0xff; slol[2] = (slol[2] * 0x49) & 0xff; break;
            case 7: slol[0] ^= 207; slol[0] = (slol[0] + 239) & 0xff; slol[0] = (slol[0] - 211) & 0xff; slol[1] = slol[1] ^ slol[0]; slol[0] = slol[1] ^ slol[0]; slol[1] = slol[1] ^ slol[0]; break;
            case 8: slol[1] = slol[1] ^ slol[2]; slol[2] = slol[1] ^ slol[2]; slol[1] = slol[1] ^ slol[2]; slol[0] = slol[0] ^ slol[1]; slol[1] = slol[0] ^ slol[1]; slol[0] = slol[0] ^ slol[1]; slol[2] = (slol[2] + 97) & 0xff; slol[1] ^= 159; break;
            case 9: slol[1] = (slol[1] * 0x61) & 0xff; slol[2] ^= 236; slol[0] = slol[0] ^ slol[2]; slol[2] = slol[0] ^ slol[2]; slol[0] = slol[0] ^ slol[2]; slol[2] = (slol[2] * 0xc7) & 0xff; break;
            case 10: slol[1] = (slol[1] - 22) & 0xff; slol[2] = (slol[2] * 0xf7) & 0xff; slol[2] = (slol[2] * 0xa3) & 0xff; slol[1] = (slol[1] * 0x3d) & 0xff; break;
            case 11: slol[1] ^= 60; slol[2] ^= 60; slol[1] = (slol[1] - 219) & 0xff; slol[0] = (slol[0] + 169) & 0xff; break;
            case 12: slol[2] ^= 21; slol[1] = (slol[1] - 247) & 0xff; slol[0] = (slol[0] * 0x29) & 0xff; slol[0] = (slol[0] + 212) & 0xff; break;
            case 13: slol[2] = (slol[2] + 221) & 0xff; slol[1] = (slol[1] * 0x2f) & 0xff; slol[2] = (slol[2] * 0xb9) & 0xff; slol[1] = (slol[1] - 192) & 0xff; break;
            case 14: slol[0] = (slol[0] * 0xc9) & 0xff; slol[2] = (slol[2] - 105) & 0xff; slol[1] = (slol[1] * 0x65) & 0xff; slol[0] ^= 158; break;
            case 15: slol[0] = (slol[0] + 110) & 0xff; slol[2] ^= 90; slol[2] = (slol[2] - 92) & 0xff; slol[1] = (slol[1] * 0xe3) & 0xff; break;
            case 16: slol[2] = (slol[2] - 151) & 0xff; slol[2] = (slol[2] * 0xf5) & 0xff; slol[1] = (slol[1] - 16) & 0xff; slol[1] = (slol[1] * 0x71) & 0xff; break;
            case 17: slol[1] = (slol[1] + 56) & 0xff; slol[0] = (slol[0] + 4) & 0xff; slol[1] = (slol[1] + 122) & 0xff; slol[0] = (slol[0] + 46) & 0xff; break;
            case 18: slol[2] = (slol[2] + 35) & 0xff; slol[2] = (slol[2] - 158) & 0xff; slol[0] ^= 105; slol[2] = (slol[2] - 89) & 0xff; break;
            case 19: slol[2] = (slol[2] * 0x2b) & 0xff; slol[0] = slol[0] ^ slol[2]; slol[2] = slol[0] ^ slol[2]; slol[0] = slol[0] ^ slol[2]; slol[0] = slol[0] ^ slol[1]; slol[1] = slol[0] ^ slol[1]; slol[0] = slol[0] ^ slol[1]; slol[0] = (slol[0] * 0x6b) & 0xff; break;
            case 20: slol[1] = slol[1] ^ slol[0]; slol[0] = slol[1] ^ slol[0]; slol[1] = slol[1] ^ slol[0]; slol[1] = slol[1] ^ slol[0]; slol[0] = slol[1] ^ slol[0]; slol[1] = slol[1] ^ slol[0]; slol[1] = (slol[1] - 142) & 0xff; slol[0] = (slol[0] + 13) & 0xff; break;
            case 21: slol[1] = slol[1] ^ slol[2]; slol[2] = slol[1] ^ slol[2]; slol[1] = slol[1] ^ slol[2]; slol[1] = (slol[1] * 0x1b) & 0xff; slol[1] = (slol[1] - 220) & 0xff; slol[0] = (slol[0] + 43) & 0xff; break;
            case 22: slol[2] = slol[2] ^ slol[0]; slol[0] = slol[2] ^ slol[0]; slol[2] = slol[2] ^ slol[0]; slol[1] = (slol[1] - 45) & 0xff; slol[1] = (slol[1] - 133) & 0xff; slol[0] = (slol[0] - 23) & 0xff; break;
            case 23: slol[2] ^= 61; slol[1] = (slol[1] + 71) & 0xff; slol[0] = (slol[0] + 185) & 0xff; slol[0] = (slol[0] - 110) & 0xff; break;
            case 24: slol[2] ^= 52; slol[2] = (slol[2] * 0x5f) & 0xff; slol[2] ^= 99; slol[2] ^= 135; break;
            case 25: slol[1] = (slol[1] - 26) & 0xff; slol[0] = (slol[0] * 0x2f) & 0xff; slol[0] ^= 24; slol[0] = (slol[0] + 163) & 0xff; break;
            case 26: slol[1] = slol[1] ^ slol[0]; slol[0] = slol[1] ^ slol[0]; slol[1] = slol[1] ^ slol[0]; slol[1] = (slol[1] * 0x79) & 0xff; slol[1] ^= 195; slol[0] ^= 170; break;
            case 27: slol[2] = (slol[2] - 132) & 0xff; slol[1] = slol[1] ^ slol[2]; slol[2] = slol[1] ^ slol[2]; slol[1] = slol[1] ^ slol[2]; slol[2] = (slol[2] + 128) & 0xff; slol[2] = (slol[2] + 33) & 0xff; break;
            case 28: slol[1] = (slol[1] - 157) & 0xff; slol[0] ^= 241; slol[2] = slol[2] ^ slol[0]; slol[0] = slol[2] ^ slol[0]; slol[2] = slol[2] ^ slol[0]; slol[2] ^= 85; break;
            case 29: slol[2] ^= 27; slol[0] = (slol[0] - 6) & 0xff; slol[2] = (slol[2] - 62) & 0xff; slol[0] = (slol[0] + 36) & 0xff; break;
        }
    }
    slol[3] = 0x00;
    printf("%s\n", slol);
    return 0;
}