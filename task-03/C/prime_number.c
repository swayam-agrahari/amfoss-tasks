#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Enter the limit: ");
    scanf("%d", &n);

    if (n < 2) {
        printf("No Prime\n");
        return 0;
    }

    printf("The prime numbers are:");
    for (int i = 2; i <= n; i++) {
        int isPrime = 1;
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                isPrime = 0;
                break;
            }
        }
        if (isPrime) {
            printf(" %d", i);
        }
    }
    printf("\n");

    return 0;
}
