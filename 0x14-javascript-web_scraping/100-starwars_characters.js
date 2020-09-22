#!/usr/bin/node
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const result = JSON.parse(body);
      for (let i = 0; i < result.characters.length; i++) {
        request(result.characters[i], function (err, resp, content) {
          if (err) {
            console.log(err);
          } else {
            if (resp.statusCode === 200) {
              const character = JSON.parse(content);
              console.log(character.name);
            }
          }
        });
      }
    }
  }
});
