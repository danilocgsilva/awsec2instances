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

* Have aws command line already installed in your system.
* Python 3 to execute and Pip to perform local installation.

## Installing

In the terminal, from the root project folder:

```
pip install .
```

## Usage

In the terminal type:
```
awsec2
```

If you have several profiles configured in your machine, then you can provide the profile:

```
awsec2 <your_profile>
```

## File list

* `awsec2instances_includes/Command_Line_Wrapper.py`: Wrappers the responsability to execute command line and split output content to the general code.

* `awsec2instances_includes/DataIterator.py`: Object that have the method to iterate through raw data from AWS Aamazon API.

* `awsec2instances_includes/DataExtractor.py`: Specialized in selecting predetermined single ec2 data from json formatted from aws api.

* `awsec2instances_includes/fn.py`: Files containing general functions.

* `awsec2instances_includes/Talk.py`: Object specialized to output information to the command line.

* `testsAssets/get_mocked_raw_data.py`: Module to provides a sample data in the same format provided by the AWS api.

* `testsAssets/get_raw_json.py`: Get a sample from real raw json from AWS api.

* `test_DataIteratorTest.py`: Class to tests the DataIterator.

* `test_Command_Line_Wrapper`: Class to tests the Comman_line_Wrapper.

* `Makefile`: scripts that uses the `make` posix like utility to make a local installation. Do not works on Windows or if the `make` utility is not installed in your system.
