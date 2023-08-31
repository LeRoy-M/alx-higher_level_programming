#!/bin/bash
# Script that sends a JSON 'POST' request and displays the body of a URL response using 'curl'
curl -sLX POST "$2" -H "Content-Type: application/json" -d "$(cat "$1")"
