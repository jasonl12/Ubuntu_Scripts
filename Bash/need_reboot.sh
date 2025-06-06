#!/usr/bin/env bash

if [ -f /var/run/reboot-required ]; then
    echo 'reboot required'
fi

cat /var/run/reboot-required.pkgs
