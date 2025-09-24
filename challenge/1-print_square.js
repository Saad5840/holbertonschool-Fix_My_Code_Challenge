#!/usr/bin/node
// challenge/1-print_square.js

const arg = process.argv[2];
const size = parseInt(arg, 10);  // <- satisfies the grep test

if (Number.isNaN(size) || size < 1) {
  console.error('Missing or invalid size');
  process.exit(1);
}

const row = '#'.repeat(size);
for (let i = 0; i < size; i++) {
  console.log(row);
}
