#!/bin/bash

A=77
B=2

#equal to
if [ $A -eq $B ]; then
  echo "A and B is equal"
fi

#not equal
if [ $A -ne $B ]; then
  echo "A and B is not equal"
fi

#less than
if [$A -le $B ]; then
  echo " A is less than B"
fi

#less or equal
if [ $A -le $b ]; then  
  echo "A is less than or equal to B"
fi

#greater than
if [ $A -gt $B ]; then
  echo "A is greater than $B"
fi

#greater or equal
if [ $A -ge $B ]; then
  echo "A is greater than or equal to B"
fi  