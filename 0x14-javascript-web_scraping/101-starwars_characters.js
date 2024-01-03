#!/usr/bin/node
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  const parsed = JSON.parse(body).characters;
  if (error) console.log(error);
  logName(parsed, 0);
});

function logName (parsed, idx) {
  request(parsed[idx], (error, response, body) => {
    if (error) console.log(error);
    console.log(JSON.parse(body).name);
    if ((idx + 1) < parsed.length) { logName(parsed, ++idx); }
  });
}
