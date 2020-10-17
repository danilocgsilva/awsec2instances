# List instances

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

Would you like to filter the listing instance by its status? Then use:
```
awsec2 -c list -r <your_region> --filter-status running
```
Then only running instances will be listed.
