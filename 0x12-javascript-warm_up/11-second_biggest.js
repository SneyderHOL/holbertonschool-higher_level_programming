#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const myArray = process.argv.slice(2);
  myArray.sort(function (a, b) { return a - b; });
  const secBiggest = myArray.length - 2;
  console.log(myArray[secBiggest]);
}
