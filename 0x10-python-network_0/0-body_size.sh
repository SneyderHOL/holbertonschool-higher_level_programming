#!/usr/bin/bash
#Bash script that takes in a URL, sends a request and display size of the body
curl -sI "$1" | grep Content-Length: | cut -d ':' -f 2 | tr -d ' '
