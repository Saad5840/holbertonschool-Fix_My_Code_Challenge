#!/usr/bin/node
// Prints a square of size given as first command-line argument.

const arg = process.argv[2];

// Validate input
const size = Number(arg);
if (Number.isNaN(size) || size < 1) {
  console.error('Missing or invalid size');
  process.exit(1);
}

// Build one line of the square
const row = '#'.repeat(size);

// Print exactly `size` rows
for (let i = 0; i < size; i++) {
  console.log(row);
}
