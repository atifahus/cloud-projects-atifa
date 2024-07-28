#!/bin/bash

bucket_exist () {
BucketName=$1  
aws s3 ls s3://$BucketName > /dev/null 2>&1
status=$?

if [ $status -eq 0 ]; then
    echo "Bucket exists"
    return 0
  else
    echo "Bucket does not exist"
    return 1
  fi
}

bucket_exist atifa-cli-bucket
bucket_exist atifa-cli-bucket9820