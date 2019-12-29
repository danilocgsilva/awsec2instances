# awsec2instances

Lists machines from AWS environment and exposes its most important informations.

## Sample output:

```
Instance count: 1
Instance Id: i-0bb06aadaed248b38
Instance type: t2.micro
PublicIp: 18.214.239.116
Name: prod
Status: running
---
Instance count: 2
Instance Id: i-0aef91c9532fbbcfd
Instance type: t2.nano
PublicIp: Sem endereco de instancia
Name: opsworks
Status: stopped
---
Instance count: 3
Instance Id: i-08ba34fc665ec536e
Instance type: t2.micro
PublicIp: 34.233.36.180
Name: test
Status: running
---
```

## Prerequisites

You must have the python3 installed in the `/usr/bin/python3` directory. Or you shall need to make changes to adapt to your environment.

## Installing

Go to root folder, and execute `sudo make`

## Usage

In the terminal type:
```
awsec2instances
```

If you have several profiles configured in your machine, then you can provide the profile:

```
awsec2instances <your_profile>
```

## File list

* `awsec2instances_includes/DataIterator.py`: Object that have the method to iterate through raw data from AWS Aamazon API.

* `awsec2instances_includes/fn.py`: Files containing general functions.

* `awsec2instances.py`: script entry file. Designed to be executed by the posix command line style or as file input to the python interpreter.

* `Makefile`: scripts that uses the `make` posix like utility to make a local installation. Do not works on Windows or if the `make` utility is not installed in your system.