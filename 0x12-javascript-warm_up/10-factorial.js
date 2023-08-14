#!/usr/bin/node
const args = process.argv;

function factorial (num) {
  if (isNaN(num) || num === undefined || num === 0) {
    return 1;
  }
  return num * factorial(--num);
}

console.log(factorial(Number(args[2])));
