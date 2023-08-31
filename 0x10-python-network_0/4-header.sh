#!/bin/bash
# Script that displays the body of a URL response with a header
# variable 'X-School-User-Id' which has value '98' using 'curl'
curl -sLX GET "$1"
