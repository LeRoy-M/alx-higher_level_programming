#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  const parsed = JSON.parse(body);
  if (error) console.log(error);

  const tasks = {};
  let completed = 0;
  for (let i = 0; i < parsed.length; i++) {
    if (parsed[i].completed === true) {
      if (!(parsed[i].userId in tasks)) {
        completed = 0;
      }
      completed++;
      tasks[parsed[i].userId] = completed;
    }
  }
  console.log(tasks);
});
