sudo apt-cache policy | grep http | awk '{print $2" "$3}' | sort -u
