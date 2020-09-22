#!/usr/bin/node
const url = process.argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/18/';
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const response = JSON.parse(body);
      const results = response.results;
      let counter = 0;
      for (let i = 0; i < results.length; i++) {
        for (let j = 0; j < results[i].characters.length; j++) {
          if (results[i].characters[j] === character) {
            counter++;
          }
        }
      }
      console.log(counter);
    }
  }
});
