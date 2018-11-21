#!/usr/bin/python
import os
import urllib2
import json
import boto3

instance_details = json.loads(urllib2.urlopen('http://169.254.169.254/2016-06-30/dynamic/instance-identity/document/').read())
instanceid=instance_details['instanceId']
REGION=instance_details['region']
ec2=boto3.client('ec2',region_name=REGION)
create_tags = ec2.create_tags(Resources=[instanceid],Tags=[{'Key':'SSM Agent','Value':'Available'}])

