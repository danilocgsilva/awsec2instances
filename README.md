# Awsec2instances

Several utilities designed to deal with ec2 operations.

Shortly, you can:

* list all vm under your account, over all regions account
* creates a vm with a service, like webserver or database

Check more in [usages](docs/_usages.md) documentation.

## Prerequisites

* Python3 interpreter
* Pip, the python package manager

Don't forget also to run `pip install -r requirements.txt` in the root folder. It is required, so assh project to handle security group also is installed.

## Installing

In the terminal, from the root project folder:

```
pip install .
```

If the operation system complains about something like *externally managed*..., ignore all of that and use:

```
pip install . --break-system-packages
```

Check [usages](docs/_usages.md).

