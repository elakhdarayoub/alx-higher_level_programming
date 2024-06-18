#!/usr/bin/node

// Check if the arg is a number
let numberOfOccur = process.argv[2];
if (isNaN(numberOfOccur)) {
  console.log('Missing number of occurrences');
} else {
  numberOfOccur = parseInt(numberOfOccur);
  for (let item = 0; item < numberOfOccur; item++) {
    console.log('C is fun');
  }
}
