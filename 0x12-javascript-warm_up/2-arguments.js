#!/usr/bin/node
let myMsg = 'No argument';
if (process.argv.length === 3) {
  myMsg = 'Argument found';
}
if (process.argv.length > 3) {
  myMsg = 'Arguments found';
}
console.log(myMsg);
