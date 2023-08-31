#!/bin/bash
# Script that displays all HTTP methods a server accepts 'curl'
curl -vX "$1" | awk "/Allow/ { print $2 }" | cut -d " " -f 2
