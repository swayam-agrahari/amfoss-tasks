use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter a positive integer n:");
    io::stdin().read_line(&mut input).expect("Failed to read input");
    let n: u32 = input.trim().parse().expect("Invalid input");

    for i in 2..n+1 {
        let mut count = 0;
        for j in 2..i {
            if i % j == 0 {
                count = 1;
                break;
            }
        }
        if count == 0 {
            println!("{}", i);
        }
    }
}
