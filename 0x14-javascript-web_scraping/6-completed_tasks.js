#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    response = JSON.parse(body);
    const obj = {};
    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        const key = response[i].userId;
        if (obj[key] === undefined) {
          obj[key] = 1;
        } else {
          obj[key] = obj[key] + 1;
        }
      }
    }
    console.log(obj);
  }
});
