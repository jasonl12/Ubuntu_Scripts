#!/usr/bin/env bash

while IFS=: read -r f1 f2 f3 f4 f5 f6 f7
do
    echo "$f1  $f7  $f6"
done < /etc/passwd
