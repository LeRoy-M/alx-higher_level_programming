#!/bin/bash
# Script that sends 'DELETE' request to URL then  displays the body of the response using 'curl'
curl -X DELETE "$1"
