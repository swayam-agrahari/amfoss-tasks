package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	fmt.Print("Enter the limit: ")
	_, err := fmt.Scan(&n)
	if err != nil || n < 2 {
		fmt.Println("No Prime")
		return
	}

	fmt.Print("The prime numbers are:")
	for i := 2; i <= n; i++ {
		count := 0
		for j := 2; j*j <= i; j++ {
			if i%j == 0 {
				count = 1
				break
			}
		}
		if count == 0 {
			fmt.Printf(" %d", i)
		}
	}
	fmt.Println() // Print a newline to end the output
}
