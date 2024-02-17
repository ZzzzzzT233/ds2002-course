d#!/bin/bash

set -3

while read line; do
echo $line;
sleep 1;
done < guids.list
