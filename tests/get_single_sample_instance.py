def get_single_sample():
    return {
        "AmiLaunchIndex": 0,
        "ImageId": "ami-35265247503565644",
        "InstanceId": "i-23716039281606134",
        "InstanceType": "t2.nano",
        "KeyName": "some-key",
        "Monitoring": {
            "State": "disabled"
        },
        "Placement": {
            "AvailabilityZone": "go-east-1g",
            "GroupName": "",
            "Tenancy": "default"
        },
        "PrivateDnsName": "ip-223-31-18-126.ec2.internal",
        "PrivateIpAddress": "223.31.18.126",
        "ProductCodes": [],
        "PublicDnsName": "",
        "State": {
            "Code": 80,
            "Name": "stopped"
        },
        "StateTransitionReason": "User initiated (2006-01-25 15:12:27 GMT)",
        "SubnetId": "subnet-9e784bec",
        "VpcId": "vpc-5b8e3328",
        "Architecture": "x86_64",
        "BlockDeviceMappings": [
            {
                "DeviceName": "/dev/xvda"
            }
        ],
        "ClientToken": "",
        "EbsOptimized": False,
        "EnaSupport": True,
        "Hypervisor": "xen",
        "NetworkInterfaces": [
            {
                "Description": "",
                "Groups": [
                    {
                        "GroupName": "opsworks",
                        "GroupId": "sg-9c779209080aa6e3f"
                    },
                    {
                        "GroupName": "default",
                        "GroupId": "sg-c870b4c2"
                    },
                    {
                        "GroupName": "dynamic_access",
                        "GroupId": "sg-0ad7abeace4f5025d"
                    },
                    {
                        "GroupName": "rds-elasticbenstalk-link",
                        "GroupId": "sg-0948ca5c00257448f"
                    }
                ],
                "Ipv6Addresses": [],
                "MacAddress": "82:48:9f:0d:2a:66",
                "NetworkInterfaceId": "eni-82a46dc2141ef7c47",
                "OwnerId": "912198172452",
                "PrivateDnsName": "ip-223-31-18-224.ec2.internal",
                "PrivateIpAddress": "223.31.18.126",
                "PrivateIpAddresses": [
                    {
                        "Primary": True,
                        "PrivateDnsName": "ip-223-31-18-126.ec2.internal",
                        "PrivateIpAddress": "223.31.18.126"
                    }
                ],
                "SourceDestCheck": True,
                "Status": "in-use",
                "SubnetId": "subnet-f403d08d",
                "VpcId": "vpc-6b4c9ddd",
                "InterfaceType": "interface"
            }
        ],
        "RootDeviceName": "/dev/xvda",
        "RootDeviceType": "ebs",
        "SecurityGroups": [
            {
                "GroupName": "aferrija",
                "GroupId": "sg-dcd0df1421b88bbe1"
            },
            {
                "GroupName": "default",
                "GroupId": "sg-afb6313b"
            },
            {
                "GroupName": "dynamic_access",
                "GroupId": "sg-bff9e22f01c993497"
            },
            {
                "GroupName": "rds-link",
                "GroupId": "sg-96c9bbc3ff184b653"
            }
        ],
        "SourceDestCheck": True,
        "StateReason": {
            "Code": "Client.UserInitiatedShutdown",
            "Message": "Client.UserInitiatedShutdown: User initiated shutdown"
        },
        "Tags": [
            {
                "Key": "Name",
                "Value": "Affer"
            },
            {
                "Key": "anotherone",
                "Value": "true"
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
        },
        "MetadataOptions": {
            "State": "applied",
            "HttpTokens": "optional",
            "HttpPutResponseHopLimit": 1,
            "HttpEndpoint": "enabled"
        },
        "EnclaveOptions": {
            "Enabled": False
        }
    }
     