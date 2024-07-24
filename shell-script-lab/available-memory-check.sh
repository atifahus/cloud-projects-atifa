#!/bin/bash

THRESHOLD=70
MEMORY=$(free -m | grep Mem | awk '{ print $7}')

if [ $MEMORY -gt $THRESHOLD ]; then
  echo "Memory is greater than Threshold"
else
  echo "Memory is not greater than Threshold"
fi  