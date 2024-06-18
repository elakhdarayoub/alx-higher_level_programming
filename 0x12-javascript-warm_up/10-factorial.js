#!/usr/bin/node

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

let number = process.argv[2];

if (isNaN(number)) {
  console.log(1);
} else {
  number = parseInt(number);
  console.log(factorial(number));
}
