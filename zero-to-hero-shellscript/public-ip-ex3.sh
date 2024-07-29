#!/bin/bash

getIpAddress () {

instance=$1

ip_address=$(aws ec2 describe-instances --instance-ids $instance --query "Reservations[*].Instances[*].[PublicIpAddress]" --output text)

if [ $? -eq 0 ]; then
  echo "The public IP Address is : $ip_address"
else
  echo "Invalid instance id is entered"
fi
}

  getIpAddress i-0ee08ff32387c87ce


#way2
ip_address=$(getIpAddress i-0ee08ff32387c87ce)
echo "Another way: " $ip_address
 