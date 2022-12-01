#!/usr/bin/node
let i = 0;

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (process.argv[2] < i) {
  process.stdout.write('');
} else {
  for (; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
