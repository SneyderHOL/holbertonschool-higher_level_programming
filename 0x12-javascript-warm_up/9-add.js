#!/usr/bin/node
const myNum1 = parseInt(process.argv[2]);
const myNum2 = parseInt(process.argv[3]);
add(myNum1, myNum2);
function add (a, b) {
  if (isNaN(myNum1) || isNaN(myNum2)) {
    console.log(NaN);
  } else {
    console.log('' + (a + b));
  }
}
