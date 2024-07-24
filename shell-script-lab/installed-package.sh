#!/bin/bash

# Define the package to check
PACKAGE="git"

if yum list installed | grep -q "$PACKAGE"; then
    echo "The package $PACKAGE is installed."
else
    echo "The package $PACKAGE is not installed."
fi