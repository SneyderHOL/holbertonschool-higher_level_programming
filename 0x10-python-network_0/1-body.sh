#!/bin/bash
#Bash script that takes in a URL, sends a GET request and displays the body
if [ "$(curl -sL -o /dev/null -w "%{http_code}\r" "$1")" == "200" ]; then curl -sL "$1"; fi
