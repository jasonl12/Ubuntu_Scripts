#!/usr/bin/env bash

l=$1
[ "$l" == "" ] && l=20
tr -dc A-Za-z0-9_ < /dev/urandom | head -c ${l} | xargs

# ./gen_pass.sh 16
