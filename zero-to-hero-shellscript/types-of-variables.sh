#!/bin/bash

#local variables
NAME="Atifa"
  echo " My name is " $NAME
 

#enviromental variables
echo " My Home Directory is: $HOME"
echo "I am logged in as: $USER"  
 

#positional variables

if [ $# -eq 2 ]; then
  echo "First argument: $1"
  echo "Second argument: $2"

else
  echo "Enter only two numbers of arguments"
fi


#special variables

  echo "Number of arguments $#"
  echo "All arguments are $@"
  echo "Exit status of the last command $?"
  echo "Process ID of the current script is $$"
  echo "Process ID of last background command is $!"
