#!/usr/bin/node

let sizeOfSquare = process.argv[2];
if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  sizeOfSquare = parseInt(sizeOfSquare);
  for (let i = 0; i < sizeOfSquare; i++) {
    for (let j = 0; j < sizeOfSquare; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
