# Remove/terminate instance

Notice: as you may know, this action will completely wipe the instance from the environment. The instace still will be there for a while with a status called `terminated`, but soon it will disapear completely from the environment.

```
awsec2 --command kill --id <your_id_instance_to_terminate>
```
or
```
awsec2 -c kill -i <your_id_instance_to_terminate>
```
If you have the awscli installed in your environment, you can achieve exactly same thing with the official awscli command to terminate:
```
aws ec2 terminate-instances --instance-ids <id_to_terminate>
```
