#!/usr/bin/node
const dict = require('./101-data').dict;
const secondDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (secondDict[value] === undefined) {
    secondDict[value] = [key];
  } else {
    secondDict[value] = secondDict[value].concat(key);
  }
}
console.log(secondDict);
