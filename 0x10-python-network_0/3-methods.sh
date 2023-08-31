#!/bin/bash
# Script that displays all HTTP methods a server accepts 'curl'
curl -vX "$1" | awk "/Allow/" | cut -d " " -f 2
