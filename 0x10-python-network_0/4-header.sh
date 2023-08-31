#!/bin/bash
# Script that displays the body of a URL response with a header variable 'X-School-User-Id' which has value '98' using 'curl'
curl -H "X-School-User-Id: 98" -sLX GET "$1"
