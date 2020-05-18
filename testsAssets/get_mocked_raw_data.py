import json

raw_string = '[{"Groups": [],"Instances": [{"AmiLaunchIndex": 0,"ImageId": "ami-0922553b7b0369273","InstanceId": "i-0aef91c9532fbbcfd","InstanceType": "t2.nano","KeyName": "main4","LaunchTime": "2019-12-15T00: 28: 08.000Z","Monitoring": {"State": "disabled"},"Placement": {"AvailabilityZone": "us-east-1c","GroupName": "","Tenancy": "default"},"PrivateDnsName": "ip-172-31-24-11.ec2.internal","PrivateIpAddress": "172.31.24.11","ProductCodes": [],"PublicDnsName": "","State": {"Code": 80,"Name": "stopped"},"StateTransitionReason": "User initiated (2019-12-15 01: 17: 30 GMT)","SubnetId": "subnet-bad9a4f0","VpcId": "vpc-202ad85a","Architecture": "x86_64","BlockDeviceMappings": [{"DeviceName": "/dev/xvda","Ebs": {"AttachTime": "2018-10-11T02: 20: 37.000Z","DeleteOnTermination": true,"Status": "attached","VolumeId": "vol-0f7285cb48ab826f5"}}],"ClientToken": "","EbsOptimized": false,"EnaSupport": true,"Hypervisor": "xen","NetworkInterfaces": [{"Attachment": {"AttachTime": "2018-10-11T02: 20: 36.000Z","AttachmentId": "eni-attach-040686e1fe6e697b8","DeleteOnTermination": true,"DeviceIndex": 0,"Status": "attached"},"Description": "","Groups": [{"GroupName": "allow-http","GroupId": "sg-04992ffa6ce8d5ff2"},{"GroupName": "default","GroupId": "sg-7fbdad34"},{"GroupName": "ssh from all","GroupId": "sg-0d3fba8e55ca910b7"}],"Ipv6Addresses": [],"MacAddress": "0a:e7: 30:c9: 39: 66","NetworkInterfaceId": "eni-085749e6eb3bb1133","OwnerId": "063695957269","PrivateDnsName": "ip-172-31-24-11.ec2.internal","PrivateIpAddress": "172.31.24.11","PrivateIpAddresses": [{"Primary": true,"PrivateDnsName": "ip-172-31-24-11.ec2.internal","PrivateIpAddress": "172.31.24.11"}],"SourceDestCheck": true,"Status": "in-use","SubnetId": "subnet-bad9a4f0","VpcId": "vpc-202ad85a","InterfaceType": "interface"}],"RootDeviceName": "/dev/xvda","RootDeviceType": "ebs","SecurityGroups": [{"GroupName": "allow-http","GroupId": "sg-04992ffa6ce8d5ff2"},{"GroupName": "default","GroupId": "sg-7fbdad34"},{"GroupName": "ssh from all","GroupId": "sg-0d3fba8e55ca910b7"}],"SourceDestCheck": true,"StateReason": {"Code": "Client.UserInitiatedShutdown","Message": "Client.UserInitiatedShutdown: User initiated shutdown"},"Tags": [{"Key": "Description","Value": "General porpouse machine to perform tasks in cloud using default Amazon ami"},{"Key": "Name","Value": "opsworks"},{"Key": "name","Value": "opsworks"}],"VirtualizationType": "hvm","CpuOptions": {"CoreCount": 1,"ThreadsPerCore": 1},"CapacityReservationSpecification": {"CapacityReservationPreference": "open"},"HibernationOptions": {"Configured": false}}],"OwnerId": "063695957269","ReservationId": "r-0fbcfc81f74a06632"},{"Groups": [],"Instances": [{"AmiLaunchIndex": 0,"ImageId": "ami-09879ea5cc6c2e899","InstanceId": "i-0c64d14a6f9bc77c8","InstanceType": "t2.micro","LaunchTime": "2019-06-23T19: 35: 57.000Z","Monitoring": {"State": "disabled"},"Placement": {"AvailabilityZone": "us-east-1c","GroupName": "","Tenancy": "default"},"PrivateDnsName": "ip-172-31-18-34.ec2.internal","PrivateIpAddress": "172.31.18.34","ProductCodes": [],"PublicDnsName": "ec2-34-196-128-99.compute-1.amazonaws.com","PublicIpAddress": "34.196.128.99","State": {"Code": 16,"Name": "running"},"StateTransitionReason": "","SubnetId": "subnet-bad9a4f0","VpcId": "vpc-202ad85a","Architecture": "x86_64","BlockDeviceMappings": [{"DeviceName": "/dev/xvda","Ebs": {"AttachTime": "2019-06-23T19: 35: 57.000Z","DeleteOnTermination": true,"Status": "attached","VolumeId": "vol-0875833ec6dbdb880"}}],"ClientToken": "6ec5ae17-59fd-840b-713a-b85e7ddfca0e_us-east-1c_1","EbsOptimized": false,"EnaSupport": true,"Hypervisor": "xen","IamInstanceProfile": {"Arn": "arn:aws:iam: : 063695957269:instance-profile/aws-elasticbeanstalk-ec2-role","Id": "AIPAIRUCSDYVR5CC4CQX2"},"NetworkInterfaces": [{"Association": {"IpOwnerId": "063695957269","PublicDnsName": "ec2-34-196-128-99.compute-1.amazonaws.com","PublicIp": "34.196.128.99"},"Attachment": {"AttachTime": "2019-06-23T19: 35: 57.000Z","AttachmentId": "eni-attach-0aa8b955c99541626","DeleteOnTermination": true,"DeviceIndex": 0,"Status": "attached"},"Description": "","Groups": [{"GroupName": "default","GroupId": "sg-7fbdad34"},{"GroupName": "awseb-e-zy5vs3mjcm-stack-AWSEBSecurityGroup-5QTY47XB9JC1","GroupId": "sg-04676e42767c1173d"}],"Ipv6Addresses": [],"MacAddress": "0a:fb: 0f: 72:e3:da","NetworkInterfaceId": "eni-02aa567755f9876a2","OwnerId": "063695957269","PrivateDnsName": "ip-172-31-18-34.ec2.internal","PrivateIpAddress": "172.31.18.34","PrivateIpAddresses": [{"Association": {"IpOwnerId": "063695957269","PublicDnsName": "ec2-34-196-128-99.compute-1.amazonaws.com","PublicIp": "34.196.128.99"},"Primary": true,"PrivateDnsName": "ip-172-31-18-34.ec2.internal","PrivateIpAddress": "172.31.18.34"}],"SourceDestCheck": true,"Status": "in-use","SubnetId": "subnet-bad9a4f0","VpcId": "vpc-202ad85a","InterfaceType": "interface"}],"RootDeviceName": "/dev/xvda","RootDeviceType": "ebs","SecurityGroups": [{"GroupName": "default","GroupId": "sg-7fbdad34"},{"GroupName": "awseb-e-zy5vs3mjcm-stack-AWSEBSecurityGroup-5QTY47XB9JC1","GroupId": "sg-04676e42767c1173d"}],"SourceDestCheck": true,"Tags": [{"Key": "aws:cloudformation:stack-name","Value": "awseb-e-zy5vs3mjcm-stack"},{"Key": "elasticbeanstalk:environment-name","Value": "danilocgsilva-me-producao-b"},{"Key": "aws:cloudformation:stack-id","Value": "arn:aws:cloudformation:us-east-1: 063695957269:stack/awseb-e-zy5vs3mjcm-stack/89404870-95ed-11e9-8cc1-0eee31812ac2"},{"Key": "aws:autoscaling:groupName","Value": "awseb-e-zy5vs3mjcm-stack-AWSEBAutoScalingGroup-ORLECDMVCP94"},{"Key": "aws:cloudformation:logical-id","Value": "AWSEBAutoScalingGroup"},{"Key": "Name","Value": "danilocgsilva-me-producao-b"},{"Key": "elasticbeanstalk:environment-id","Value": "e-zy5vs3mjcm"}],"VirtualizationType": "hvm","CpuOptions": {"CoreCount": 1,"ThreadsPerCore": 1},"CapacityReservationSpecification": {"CapacityReservationPreference": "open"},"HibernationOptions": {"Configured": false}}],"OwnerId": "063695957269","RequesterId": "940372691376","ReservationId": "r-09d8d28e57acff374"}]'


def get_mocked_raw_data():
    return json.loads(raw_string)


def check_raw_json():
    return raw_string
