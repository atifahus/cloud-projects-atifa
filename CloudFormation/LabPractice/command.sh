#validation:
aws cloudformation validate-template\
    --template-body file://9-manageOutputs.yaml

aws cloudformation create-stack --stack-name bucketWithIfCondition\
    --template-body file://1-createS3Bucket.yaml\
    --parameters file://param.json\
    --capabilities CAPABILITY_IAM


aws cloudformation create-stack --stack-name dependsOnSG\
      --template-body file://5-dependsOn.yaml\
      --capabilities CAPABILITY_IAM


#7
aws cloudformation create-stack --stack-name bucketWithSub\
    --template-body file://7-fnSub.yaml\
    --parameters file://param.json\
    --capabilities CAPABILITY_IAM

#9
aws cloudformation create-stack --stack-name lab9\
      --template-body file://9-manageOutputs.yaml\
      --capabilities CAPABILITY_IAM

#10
aws cloudformation create-stack --stack-name lab10-b\
       --template-body file://10-b-import.yaml\
       --capabilities CAPABILITY_IAM


#11
aws cloudformation create-stack --stack-name updateAuto\
      --template-body file://11-updatePolicy.yaml\
      --capabilities CAPABILITY_IAM

#13
aws cloudformation create-stack --stack-name ec2Tag\
      --template-body file://13-TagsManagement.yaml\
      --capabilities CAPABILITY_IAM

#14
aws cloudformation create-stack --stack-name bucketDelettion\
    --template-body file://14-deletionPolicy.yaml\
    --capabilities CAPABILITY_IAM