#!/usr/bin/env bash

# dpkg -L package
dpkg --get-selections | awk '/deinstall/ {print $1}' | xargs -n1 sudo dpkg --purge

sudo apt autoremove -y
sudo apt autoclean -y
sudo apt clean -y
