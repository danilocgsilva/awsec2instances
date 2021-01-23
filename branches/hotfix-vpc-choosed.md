# hotfix/vpc-choosed

When creating a new instance in a VPC with several VPCs, there's an error:
```
Traceback (most recent call last):
  File "/usr/local/bin/awsec2", line 8, in <module>
    sys.exit(main())
  File "/home/danilo/.local/lib/python3.8/site-packages/awsec2instances_includes/__main__.py", line 61, in main
    create_new_instance(args, commands)
  File "/home/danilo/.local/lib/python3.8/site-packages/awsec2instances_includes/fn.py", line 79, in create_new_instance
    vpc_choosed,
UnboundLocalError: local variable 'vpc_choosed' referenced before assignment
```

