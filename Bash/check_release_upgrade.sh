#!/usr/bin/env bash

set -eu

# Source the os-release file
if [ -f /etc/os-release ]; then
    . /etc/os-release
    if [ "$ID" != "ubuntu" ]; then
        echo "This is not an Ubuntu system."
        exit 1
    fi
fi

if [ $(id -u) -eq 0 ]; then
    echo "Updating package index files ..."
    apt-get -qq update
    apt list --upgradable
    echo "" && lsb_release -src
    uname -mrs

    if command -v do-release-upgrade &> /dev/null; then
        which do-release-upgrade
    else
        echo "do-release-upgrade not found"
        # sudo apt-get download ubuntu-release-upgrader-core
        # dpkg-deb -x ubuntu-release-upgrader-core_1%3a22.04.20_all.deb ./
        echo "ubuntu-release-upgrader-core is not installed."
    fi

    echo "" && df -Th /
    echo "" && grep -r -h "^deb" /etc/apt/sources.list /etc/apt/sources.list.d | grep -v "ubuntu" | sort -u
    echo ""
    echo "Running services: " && systemctl -t service | grep running | wc -l
    echo ""

    # command (POSIX command); https://en.wikipedia.org/wiki/List_of_POSIX_commands
    if command -v apache2 &> /dev/null; then
        echo "apache2 is installed."
    fi

    if command -v nginx &> /dev/null; then
        echo "nginx is installed."
    fi

    if command -v mysql &> /dev/null; then
        echo "mysql (mariadb) is installed."
    fi

    if command -v psql &> /dev/null; then
        echo "psql is installed."
    fi

    echo ""
    df -Th | grep -E "cifs|nfs"
else
    echo "Not running as root or with sudo"
fi
