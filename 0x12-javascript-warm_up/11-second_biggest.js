#!/usr/bin/node
const args = process.argv;

if (args.length > 3) {
  let firB = 0; let secB;
  for (let i = 2; i < args.length; i++) {
    if (Number(args[i]) > firB) {
      secB = firB;
      firB = args[i];
    } else if (Number(args[i]) > secB) {
      secB = args[i];
    }
  }
  console.log(secB);
} else {
  console.log(0);
}
