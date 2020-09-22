#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let occurrenceNumber = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurrenceNumber++;
    }
  }
  return occurrenceNumber;
};
