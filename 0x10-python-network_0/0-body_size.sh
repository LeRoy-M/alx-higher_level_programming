#!/bin/bash
# Script that displays the size of the body of a URL response using 'curl'
curl -sI $1 | awk "/Content-Length/ { print $2 }"
