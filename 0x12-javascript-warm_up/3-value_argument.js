#!/usr/bin/node
let myMsg = 'No argument';
if (process.argv[2] !== undefined) {
  myMsg = process.argv[2];
}
console.log(myMsg);
