#!/bin/bash

THRESHOLD=20

USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

if [ "$USAGE" -gt "$THRESHOLD" ]; then
    echo "Warning: Disk usage is above $THRESHOLD%."
else
    echo "Disk usage is below $THRESHOLD%."
fi

# df / | grep / | awk '{ print $5 }' | sed 's/%//g'
# Filesystem     1K-blocks    Used Available Use% Mounted on
#devtmpfs            4096       0      4096   0% /dev
# tmpfs             486156       0    486156   0% /dev/shm
#tmpfs             194464     448    194016   1% /run
#/dev/xvda1       8310764 1901816   6408948  23% /
# tmpfs             486160       0    486160   0% /tmp
# /dev/xvda128       10202    1310      8892  13% /boot/efi
# tmpfs              97228       0     97228   0% /run/user/1000

#sh types-of-variables.sh 1 4
#input to the script types-of-variables.sh are 1 and 4 
# and if we like to utilize these inputs we gonna call them $1 and $2