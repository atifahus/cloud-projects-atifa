#!/bin/bash
echo "test"
USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Warning: Disk usage is above $THRESHOLD%."
else
    echo "Disk usage is below $THRESHOLD%."
fi