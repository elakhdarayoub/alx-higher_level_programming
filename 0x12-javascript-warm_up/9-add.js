#!/usr/bin/node

let firstNum = process.argv[2];
let secondNum = process.argv[3];

if (isNaN(firstNum) || isNaN(secondNum)) {
  console.log('NaN');
} else {
  firstNum = parseInt(firstNum);
  secondNum = parseInt(secondNum);

  console.log(firstNum + secondNum);
}
