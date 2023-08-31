#!/bin/bash
# Script that displays all HTTP methods a server accepts 'curl'
curl -iX OPTIONS "$1"
