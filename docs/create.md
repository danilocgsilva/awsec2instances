# Create instance

You may want create a new instance...

```
awsec2 --command new
```
or
```
awsec2 -c new
```

You may want create and access it by ssh
```
awsec2 --command new --access with-ssh
```
Note: your instance needs to have an keypair to be accessed by ssh. Just have one in your aws account and it will be automatically fetched.

Or want to access by http address:
```
awsec2 --command new --access with-http
```
Note: your instance must have an webserver software installed and running to trully access the instance by web.

You can set several types of access at once:
```
awsec2 --command new --access with-http,with-http
```
And both access by http and ssh will be enabled.

You may need a webserver. In this case, type:
```
awsec2 --command new --user-data webserver
```
Then after the new instance is created, you will be able to reach it by web, typing its ip in the browser.
```

Want a better identification your just created instance? The use:
```
awsec2 --command new --name my-favourite-vm
```
And the new VM will have an tag name with the name setted.

By default, for shrinks the risk of setting an useless instance in mistake, the instance just created will be setted to lasts for just 5 minutes.

You may need an instance to be up for longer time. To do so, just type:

```
awsec2 --command new --lasts 60
```
Then you set 60 minutes to stay alive. If you really want very long time, there are other values to put as parameter:

```
awsec2 --command new --lasts for-ten-minutes
awsec2 --command new --lasts for-an-hour
awsec2 --command new --lasts for-a-day
awsec2 --command new --lasts for-an-week
awsec2 --command new --lasts for-a-month
awsec2 --command new --lasts for-an-year
awsec2 --command new --lasts forever
```
