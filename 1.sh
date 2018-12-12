#!/bin/bash

read -p 'please input a nunmber' n
echo n

if [ $n -gt 5 ]
then
    echo 'biger than five'
else
    echo 'false'
fi
