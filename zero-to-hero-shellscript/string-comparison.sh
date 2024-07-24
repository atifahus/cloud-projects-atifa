#!/bin/bash

FRUIT="Apple"
COST="Five"
QUALTITY=" "
SNACK="Apple"
a="qwe"


#equal
if [ "$FRUIT" = "$SNACK" ]; then
  echo "Fruit and Snack string are equal"
fi

#not equal
if [[ "$FRUIT" != "$COST" ]]; then
  echo "Fruit and Price string is not equal"
fi

#less than
if [[ "$FRUIT" < "$COST" ]]; then
  echo "Fruit string is less than Price string"
fi

#greater than
if [ "$FRUIT" > "$a" ]; then
  echo "Fruit string is greater than Quality string"
fi

#string is empty
if [ -z $QUALTITY ]; then
  echo "Variable is null"
fi  

#string is not null
if [ -n $FRUIT ]; then
  echo "Variable is not null"
fi