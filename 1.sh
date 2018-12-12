#!/bin/bash

read -p 'please input a nunmber' n
echo n

if [ $n -gt 4] 
then
    echo 'true'
else
    echo 'false'
fi
