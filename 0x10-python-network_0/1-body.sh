#!/bin/bash
#Bash script that takes in a URL, sends a GET request and displays the body
if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" == "200" ]; then curl -s "$1"; fi
