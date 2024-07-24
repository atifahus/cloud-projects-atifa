#!/bin/bash

FILE="shell-practice-test.txt"

#file exist
if [ -e $FILE ]; then
  echo "$FILE exists"
fi  


#regular file
if [ -f $FILE ]; then
  echo "$FILE is a regular file"
fi

#not empty
if [ -s $FILE ]; then
  echo "$FILE is not empty"
fi

#readable
if [ -r $FILE ]; then
  echo "$FILE is readable"
fi

#writable
if [ -w $FILE ]; then
  echo "$FILE is writable"
fi

#executable
if [ -x $FILE ]; then
  echo "$FILE is executable"
fi