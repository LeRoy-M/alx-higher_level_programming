#!/usr/bin/node
process.argv.shift();
process.argv.shift();
process.argv.sort(function (a, b) { return a - b; });

if (process.argv.length < 2) {
  console.log('0');
} else {
  console.log(process.argv[process.argv.length - 2]);
}
