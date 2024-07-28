#!/bin/bash
BUCKET="atifatestingaws"


aws s3 ls "s3://atifatestingaws" | awk -F 'ListObjectsV2' '{ print $2 }' | awk '{print $1}' 

aws s3 ls "s3://atifatestingaws" | sed 's/)//g'

awk -F 'load average:' '{ print $2 }'| awk '{print $1}'| sed 's/,//g'