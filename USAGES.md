# Usages

## List instances

In the terminal type:
```
awsec2
```

Your environment may require a profile name:
```
awsec2 --profile <some_profile>
```

If you want to restrict information for just a single region, type:

```
awsec2 --region <your_region>
```
or
```
awsec2 -r <your_region>
```

## Create new instance

You may want create a new instance...

```
awsec2 --command new
```
or
```
awsec2 -c new
```

## Removing/terminating an instance

```
awsec2 --command kill --id-to-kill <your_id_instance_to_terminate>
```
or
```
awsec2 -c kill -ik <your_id_instance_to_terminate>
```
If you have the awscli installed in your environment, you can achieve exactly same thing with the official awscli command to terminate:
```
aws ec2 terminate-instances --instance-ids <id_to_terminate>
```

## Start stopped instance

```
awsec2 --command restart --id-to-restart <your_id_instance_to_restart>
```
or
```
awsec2 -c restart -ir <your_id_instance_to_restart>
```
