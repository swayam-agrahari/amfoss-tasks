#include <iostream>
#include <cmath>

using namespace std; 

int main() {
    int n;
    cout << "Enter the limit: ";
    cin >> n;

    if (n < 2) {
        cout << "No Prime" << endl;
        return 0;
    }

    cout << "The prime numbers are:";
    for (int i = 2; i <= n; i++) {
        bool isPrime = true;
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            cout << " " << i;
        }
    }
    cout << endl;

    return 0;
}

