#!/bin/bash
#Bash script that sends a JSON POST to a URL
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
