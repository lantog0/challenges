#include <stdio.h>

int main()
{
    char key[] = {97, 77, 53, 73, 107, 80, 52, 65, 100, 81};
    const char charset[] = 
    "abcdefghijklmnopqrstuvwxyz"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "123456789";

    int c_size = sizeof(charset) - 1;
    int k_size = sizeof(key);

    unsigned int holdrand, enc;
    int j, i;
 
    for (i = 1354320000; i < 1356998399; i++) {
        holdrand = i;
        j = 0;

        while (j < k_size) {
            holdrand = holdrand * 214013L + 2531011L;
            enc = ((holdrand >> 16) & 0x7fff) % c_size;

            if (key[j] == charset[enc])
                j++;
            else
                break;
        }

        if (j == k_size) {
            printf("Found key! %d\n", i);
            break;
        }
    }

    return 0;
}
