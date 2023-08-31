#!/bin/bash
# Script that displays the status code of a URL response using 'curl'
curl -so /dev/null -w "%{http_code}"  "$1"
