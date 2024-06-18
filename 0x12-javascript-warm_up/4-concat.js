#!/usr/bin/node

const args = process.argv;
if (args.length < 4) {
  console.log('Not enough argument');
} else if (args.length > 4) {
  console.log('Too much arguments');
} else {
  console.log(args[2] + ' is ' + args[3]);
}
