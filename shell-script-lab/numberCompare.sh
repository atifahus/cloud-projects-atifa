#!/bin/bash

NUM1=18
NUM2=44
#if num 1 is equal to num2

if [ "$NUM1" -eq "$NUM2" ]; then
	echo "NUM1 is equal to NUM2"
else


	echo "NUM1 is not equal to NUM2"
fi

#if num1 is greater than num2

if [ "$NUM1" -gt "$NUM2" ]; then
	echo "NUM1 is greater than NUM2"
else
	echo "NUM1 is not greater than NUM2"
fi

#if num1 is less than num2

if [ "$NUM1" -lt "$NUM2" ]; then
        echo "NUM1 is less than NUM2"
else
    	echo "NUM1 is not less than NUM2"
fi

