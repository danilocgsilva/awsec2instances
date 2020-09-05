# Create instance

You may want create a new instance...

```
awsec2 --command new
```
or
```
awsec2 -c new
```

**(still not implemented yet)** You may want create and access it by ssh
```
awsec2 --command new --access with-ssh
```
Note: your instance needs to have an keypair to be accessed by ssh.

Or want to access by http address:
```
awsec2 --command new --access with-http
```
Note: your instance must have an webserver software installed and running to trully access the instance by web.
