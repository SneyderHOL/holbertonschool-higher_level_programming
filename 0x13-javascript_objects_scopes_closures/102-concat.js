#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');
const res1 = fs.readFileSync(fileA, 'utf8');
const res2 = fs.readFileSync(fileB, 'utf8');
fs.writeFile(fileC, res1 + res2, function (err) {
  if (err) return console.log(err);
});
