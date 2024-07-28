#!/bin/bash

get_instance_id () {


result=$(aws ec2 describe-instances --filters Name=instance-type,Values=t2.micro --query  "Reservations[*].Instances[*].[InstanceId]" --output text)


echo "The list of the EC2 instance are: " 
echo $result | tr ' ' '\n'
}


get_instance_id 
