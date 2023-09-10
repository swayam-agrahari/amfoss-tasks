const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter the limit: ', (answer) => {
  const n = parseInt(answer);

  if (isNaN(n) || n < 2) {
    console.log('No Prime');
    rl.close();
    return;
  }

  console.log('The prime numbers are:');
  for (let i = 2; i <= n; i++) {
    let count = 0;
    for (let j = 2; j * j <= i; j++) {
      if (i % j === 0) {
        count = 1;
        break;
      }
    }
    if (count === 0) {
      process.stdout.write(` ${i}`);
    }
  }
  console.log(); // Print a newline to end the output
  rl.close();
});

