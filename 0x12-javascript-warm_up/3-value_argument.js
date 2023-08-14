#!/usr/bin/node
const args = process.argv;

if (args[1]) {
  console.log(args[1]);
} else {
  console.log('No argument');
}
