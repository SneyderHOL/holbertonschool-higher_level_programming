#!/usr/bin/bash
#Bash script that takes in a URL, sends a GET request and displays the body
result=$(curl -sI "$1" -X GET -w http-out)
status=$(echo "$result" | grep HTTP/ | cut -d " " -f 2)
if [ "$status" == "200" ]; then
    curl "$1"
fi
