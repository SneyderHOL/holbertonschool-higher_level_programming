#!/usr/bin/node
let number = 0;

module.exports.logMe = function (item) {
  console.log(number + ': ' + item);
  number++;
};
