#!/bin/bash
THRESHOLD=1.0
LOAD=$(uptime | awk -F 'load average:' '{ print $2 }'| awk '{print $1}'| sed 's/,//g')

if (( $(echo "$LOAD > $THRESHOLD" | bc -l) )); then
 echo "Warning: CPU load is above $THRESHOLD."
else
    echo "CPU load is below $THRESHOLD."
fi