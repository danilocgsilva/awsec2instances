# Create instance

* [Creating new instance](#Creating-new-instance)
* [Setting a distro](#Setting-a-distro)
* [Accessing new created instance](Accessing-new-created-instance)
* [Creating an instance by some common role](#Creating-an-instance-by-some-common-role)
* [Setting instances to live more than just 5 minutes](#Setting-instances-to-live-more-than-just-5-minutes)
* [Give a name to the instance](#Give-a-name-to-the-instance)

## Creating new instance

You may want create a new instance...

```
awsec2 --command new
```
or
```
awsec2 -c new
```

Want a better identification your just created instance? The use:
```
awsec2 --command new --name my-favourite-vm
```
And the new VM will have an tag name with the name setted.

## Setting a distro

By default, an instance will be created based on the AWS default system imagem.

But if you would like to rise an Ubuntu Server, just do:

```
awsec2 --command new --distro ubuntu
```

## Accessing new created instance

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


## Creating an instance by some common role

You may need a webserver. In this case, type:
```
awsec2 --command new --user-data webserver
```
Then after the new instance is created, you will be able to reach it by web, typing its ip in the browser.

(NOT IMPLEMENTED YET) Want just a database node?
```
awsec2 --command new --user-data database
```

(NOT IMPLEMENTED YET) You can raise an instance to be acessed by graphical interface. Them just type:
```
awsec2 --command new --user-data desktop
```

Other options for specific role:

```
awsec2 --command new --user-data wordpress
```
Creates an AWS instance with Wordpress installed.

```
awsec2 --command new --user-data laravel
```
Creates an AWS instance with Laravel installed

## Setting instances to live more than just 5 minutes

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


## Give a name to the instance

You can set a tag to your instance with the key *name*, so it is easier so you can set a more friendly name to identify the instance.

```
awsec2 -n my-instance-with-web-application
```
