#!/bin/bash

#way 1
function sum () {
A=$1
B=$2
RESULT=$((A+B))
echo $RESULT
}


RESULT=$(sum 3 5)

echo $RESULT

#way 2
multiply () {
N=2
M=5
res=$((N*M))
echo $res
}

multiply

#way 3
division () {
X=$1
Y=$2
r=$((X/Y))
echo "X divided by Y is $r "
}
division 6 3

#return 
student() {
NAME="John"
echo "My name is $NAME"
return 21
}

student

age=$?
echo "$NAME's age is $age"
