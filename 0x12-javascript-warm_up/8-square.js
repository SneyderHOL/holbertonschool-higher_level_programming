#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
let myMsg = '';
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNum; i++) {
    for (let j = 0; j < myNum; j++) {
      myMsg = myMsg + 'X';
    }
    if (i < (myNum - 1)) {
      myMsg = myMsg + '\n';
    }
  }
  console.log(myMsg);
}
