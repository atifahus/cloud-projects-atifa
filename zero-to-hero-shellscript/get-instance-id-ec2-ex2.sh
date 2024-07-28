#!/bin/bash

get_instance_id () {
TAG_NAME=$1
TAG_VALUE=$2

result=$(aws ec2 describe-instances --filters Name=tag:$TAG_NAME,Values=$TAG_VALUE --query  "Reservations[*].Instances[*].[InstanceId]" --output text)

echo "Instance ID for $TAG_NAME is:  $result"

}


get_instance_id Role fullAccessS3ForInstance