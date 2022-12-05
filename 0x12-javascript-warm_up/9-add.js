#!/usr/bin/node
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}

console.log(add(a, b));
