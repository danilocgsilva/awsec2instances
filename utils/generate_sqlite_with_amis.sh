#!/bin/bash

if [ -z $1 ]; then
    echo You need to provides a first argument to be the aws profile.
    exit
fi

if [ -z $2 ]; then
    echo You need the second argument to be the region from with you need get the amis data.
    exit
fi

echo Fetching json data...
python3 ../activeTests/get_all_amis.py --profile $1 --region $2 > /tmp/tmpamis.json
ree_ct < /tmp/tmpamis.json > /tmp/tmpcreate.sql
echo Generating insert script...
ree_is < /tmp/tmpamis.json > /tmp/tmpinsert.sql
sqlite3 amis.db << EOF
    .read /tmp/tmpcreate.sql;
    .read /tmp/tmpinsert.sql;
EOF
