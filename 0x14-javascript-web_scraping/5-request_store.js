#!/usr/bin/node
const url = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(file, response.body, function (err) {
        if (err) {
          console.log(err);
        }
      });
      console.log(response.body);
    }
  }
});
