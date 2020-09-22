#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const secondList = list.map(function (num, index) {
  return num * index;
});
console.log(secondList);
