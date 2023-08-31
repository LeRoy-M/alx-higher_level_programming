#!/bin/bash
# Script that displays the size of the body of a URL response using 'curl'
curl -sI "$1" | awk "/[Cc]ontent-[Ll]ength/ { print $2 }" | cut -d " " -f 2
