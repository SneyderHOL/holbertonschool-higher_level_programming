#!/bin/bash
#Bash script that takes in a URL and displays all HTTTP methods
curl -sIL "$1" | grep Allow | cut -d ' ' -f 2-
