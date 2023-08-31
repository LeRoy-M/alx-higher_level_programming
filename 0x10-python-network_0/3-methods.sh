#!/bin/bash
# Script that displays all HTTP methods a server accepts 'curl'
curl -vX OPTIONS "$1"
