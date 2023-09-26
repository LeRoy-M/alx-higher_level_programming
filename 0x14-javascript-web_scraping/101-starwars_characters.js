#!/usr/bin/node
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  const parsed = JSON.parse(body).characters;
  if (error) console.log(error);

  for (let i = 0; i < parsed.length; i++) {
    request(parsed[i], (error, response, body) => {
      const character = JSON.parse(body).name;
      if (error) console.log(error);
      console.log(character);
    });
  }
});
