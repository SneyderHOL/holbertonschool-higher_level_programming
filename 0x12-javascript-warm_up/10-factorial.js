#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
console.log(factorial(myNum));
function factorial (num) {
  if ((isNaN(num)) || (num === 1)) {
    return 1;
  }
  return num * factorial(num - 1);
}
