#!/bin/bash
#Bash script that takes in a URL, sends a GET request and displays the body
curl -sL -o /dev/null -w "%{http_code}" "$1"
