mocked_single_instance_data = {
    "AmiLaunchIndex": 0,
    "ImageId": "ami-0922553b7b0369273",
    "InstanceId": "i-0aef91c9532fbbcfd",
    "InstanceType": "t2.nano",
    "KeyName": "main4",
    "LaunchTime": "2019-12-15T00: 28: 08.000Z",
    "Monitoring": {
        "State": "disabled"
    },
    "Placement": {
        "AvailabilityZone": "us-east-1c",
        "GroupName": "",
        "Tenancy": "default"
    },
    "PrivateDnsName": "ip-172-31-24-11.ec2.internal",
    "PrivateIpAddress": "172.31.24.11",
    "ProductCodes": [],
    "PublicDnsName": "",
    "State": {
        "Code": 80,
        "Name": "stopped"
    },
    "StateTransitionReason": "User initiated (2019-12-15 01: 17: 30 GMT)",
    "SubnetId": "subnet-bad9a4f0",
    "VpcId": "vpc-202ad85a",
    "Architecture": "x86_64",
    "BlockDeviceMappings": [
        {
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "AttachTime": "2018-10-11T02: 20: 37.000Z",
                "DeleteOnTermination": True,
                "Status": "attached",
                "VolumeId": "vol-0f7285cb48ab826f5"
            }
        }
    ],
    "ClientToken": "",
    "EbsOptimized": False,
    "EnaSupport": True,
    "Hypervisor": "xen",
    "NetworkInterfaces": [
        {
            "Attachment": {
                "AttachTime": "2018-10-11T02: 20: 36.000Z",
                "AttachmentId": "eni-attach-040686e1fe6e697b8",
                "DeleteOnTermination": True,
                "DeviceIndex": 0,
                "Status": "attached"
            },
            "Description": "",
            "Groups": [
                {
                    "GroupName": "allow-http",
                    "GroupId": "sg-04992ffa6ce8d5ff2"
                },
                {
                    "GroupName": "default",
                    "GroupId": "sg-7fbdad34"
                },
                {
                    "GroupName": "ssh from all",
                    "GroupId": "sg-0d3fba8e55ca910b7"
                }
            ],
            "Ipv6Addresses": [],
            "MacAddress": "0a:e7: 30:c9: 39: 66",
            "NetworkInterfaceId": "eni-085749e6eb3bb1133",
            "OwnerId": "063695957269",
            "PrivateDnsName": "ip-172-31-24-11.ec2.internal",
            "PrivateIpAddress": "172.31.24.11",
            "PrivateIpAddresses": [
                {
                    "Primary": True,
                    "PrivateDnsName": "ip-172-31-24-11.ec2.internal",
                    "PrivateIpAddress": "172.31.24.11"
                }
            ],
            "SourceDestCheck": True,
            "Status": "in-use",
            "SubnetId": "subnet-bad9a4f0",
            "VpcId": "vpc-202ad85a",
            "InterfaceType": "interface"
        }
    ],
    "RootDeviceName": "/dev/xvda",
    "RootDeviceType": "ebs",
    "SecurityGroups": [
        {
            "GroupName": "allow-http",
            "GroupId": "sg-04992ffa6ce8d5ff2"
        },
        {
            "GroupName": "default",
            "GroupId": "sg-7fbdad34"
        },
        {
            "GroupName": "ssh from all",
            "GroupId": "sg-0d3fba8e55ca910b7"
        }
    ],
    "SourceDestCheck": True,
    "StateReason": {
        "Code": "Client.UserInitiatedShutdown",
        "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
    },
    "Tags": [
        {
            "Key": "Description",
            "Value": "General porpouse machine to perform tasks in cloud using default Amazon ami"
        },
        {
            "Key": "Name",
            "Value": "opsworks"
        },
        {
            "Key": "name",
            "Value": "opsworks"
        }
    ],
    "VirtualizationType": "hvm",
    "CpuOptions": {
        "CoreCount": 1,
        "ThreadsPerCore": 1
    },
    "CapacityReservationSpecification": {
        "CapacityReservationPreference": "open"
    },
    "HibernationOptions": {
        "Configured": False
    }
}