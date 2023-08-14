#!/usr/bin/node
const args = process.argv;

if (!isNaN(args[2])) {
  for (let i = 0; i < Number(args[2]); i++) {
    let size = '';
    for (let j = 0; j < Number(args[2]); j++) {
      size += 'X';
    }
    console.log(size);
  }
} else {
  console.log('Missing size');
}
