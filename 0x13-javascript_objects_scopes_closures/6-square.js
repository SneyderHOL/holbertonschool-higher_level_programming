#!/usr/bin/node
const SquareModel = require('./5-square');
class Square extends SquareModel {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let symbol = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          symbol += c;
        }
        if (i < (this.height - 1)) {
          symbol += '\n';
        }
      }
      console.log(symbol);
    }
  }
}
module.exports = Square;
