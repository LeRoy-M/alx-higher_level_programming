#!/usr/bin/node
const f = parseInt(process.argv[2]);

function factorial (f) {
  if (isNaN(f) || f === undefined || f === 0) {
    return 1;
  }

  return f * factorial(f - 1);
}

console.log(factorial(f));
