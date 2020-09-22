#!/usr/bin/node
const file = process.argv[2];
const fs = require('fs');
try {
  const content = fs.readFileSync(file, 'utf8');
  console.log(content);
} catch (err) {
  console.log(err);
}
