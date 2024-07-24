#!/bin/bash

BUCKETNAME="atifa-cli-bucket"
FILENAME="shell-practice-test/txt"

aws s3 mb s3://$BUCKETNAME

aws s3 cp $FILENAME s3://$BUCKETNAME/testFile.txt

echo "$FILENAME file has been uploaded to $BUCKETNAME bucket"
