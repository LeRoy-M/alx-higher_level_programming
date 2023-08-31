#!/bin/bash
# Script that sends a 'POST' request and displays the body of a URL response using 'curl'
curl -H "email: test@gmail.com" "subject: I will always be here for PLD" -sLX POST "$1"
