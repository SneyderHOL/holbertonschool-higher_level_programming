#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
let myMsg = 'My number: ' + myNum;
if (isNaN(myNum)) {
  myMsg = 'Not a number';
}
console.log(myMsg);
