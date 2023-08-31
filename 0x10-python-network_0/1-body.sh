#!/bin/bash
# Script that displays the body of a URL response using 'curl'
code=$(curl -so  /dev/null -Iw "%{http_code}" "$1")

if [ "$code" -eq 200 ]; then
	curl -sL "$1"
fi
