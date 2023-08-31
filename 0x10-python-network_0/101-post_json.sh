#!/bin/bash
# Script that sends a JSON 'POST' request and displays the body of a URL response using 'curl'
curl -sLX POST -H "Content-Type: application/json" -d "$2" "$(cat "$1")"
