#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  const parsed = JSON.parse(body);
  if (error) console.log(error);

  const cmpdTasks = {};
  for (let i = 0; i < parsed.length; i++) {
    if (parsed[i].completed) {
      if (!(parsed[i].userId in cmpdTasks)) { cmpdTasks[parsed[i].userId] = 1; } else { cmpdTasks[parsed[i].userId]++; }
    }
  }
  console.log(cmpdTasks);
});
