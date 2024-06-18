#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let biggest = parseInt(args[2]);
  let second;
  for (let num = 2; num < args.length; num++) {
    if (parseInt(args[num]) > biggest) {
      second = biggest;
      biggest = parseInt(args[num]);
    }
  }
  console.log(second);
}
