#!/usr/bin/env bash
# A Simple Shell Script To Clean Logs (flexibility on different systems)

sudo find /var/log/ -type f -regex '.*\.[0-9]+\.gz$'
DEL="sudo find /var/log/ -type f -regex '.*\.[0-9]+\.gz$' -delete"
echo ""

# -p prompt
read -p "Do you want to delete these files? [Yes/No]" yn

case $yn in
  [Yy]* ) echo "Delete ..." && eval $DEL && exit;;
  [Nn]* ) echo "Cancel" && exit;;
esac
