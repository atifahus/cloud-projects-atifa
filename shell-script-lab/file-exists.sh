#!/bin/bash
FILE="list.txt"

if [ -e "$FILE" ]; then
	echo "File exists"
else
	echo "File doesn't exists"
fi
