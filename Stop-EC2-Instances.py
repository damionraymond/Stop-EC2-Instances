import json
import boto3

#Indicate what region your instances are running
region = 'us-east-1'

#Incude the Instance Id of each instance you want stopped
instances = ['i-0c1a727300375b312', 'i-05c2b6ff0d9634879','i-0bb4e950eb0d77055']

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))