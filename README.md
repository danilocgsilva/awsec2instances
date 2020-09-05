# awsec2instances

Lists machines from AWS environment and exposes its most important informations.
Loops through all regions, so no lost ec2 will be out from your eyes.

## Sample output:

```
Getting data from region ap-southeast-2
Getting data from region eu-central-1
Getting data from region us-east-1
---
Instance counting: 1
Id: i-9876f9d987a9876f
Name: MyEcName
Status: stopped
Type: t2.nano
Ip: ---
---
Instance counting: 2
Id: i-004f12d45a7b7
Name: WindowsCloud
Status: stopped
Type: t2.micro
Ip: ---
---
Instance counting: 3
Id: i-834f2a1b56c775
Name: cloudWorks
Status: stopped
Type: t2.nano
Ip: ---
---
Instance counting: 4
Id: i-542fb23c5de564f
Name: this-is-turned-on
Status: running
Type: t2.micro
Ip: 34.196.128.99
Getting data from region us-east-2
Getting data from region us-west-1
Getting data from region us-west-2
---
```

## Prerequisites

* Python 3 to execute and Pip to perform local installation.

## Installing

In the terminal, from the root project folder:

```
pip install .
```

Check [usages](docs/_usages.md).

