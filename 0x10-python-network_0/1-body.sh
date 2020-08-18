#!/usr/bin/env bash
#Bash script that takes in a URL, sends a GET request to the URL and displays
#the body of the response
result=$(curl -sI "$1" -X GET)
status=$(echo "$result" | grep HTTP/ | cut -d " " -f 2)
if [ "$status" == "200" ]; then
    curl "$1"
fi
