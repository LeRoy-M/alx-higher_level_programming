#!/usr/bin/node

const args = process.argv;
const fs = require('fs');
const src1 = fs.readFileSync(args[2], 'utf-8');
const src2 = fs.readFileSync(args[3], 'utf-8');
fs.writeFileSync(args[4], src1 + src2);
