#!/bin/bash

sudo sysctl -a | grep -e "vm.swappiness" \
-e "vm.dirty_ratio" \
-e "vm.dirty_background_ratio" \
-e "net.core.somaxconn" \
-e "net.ipv4.tcp_fin_timeout" \
-e "net.ipv4.tcp_tw_reuse"


# net.core.somaxconn = 4096
# net.ipv4.tcp_fin_timeout = 60
# net.ipv4.tcp_tw_reuse = 2
# vm.dirty_background_ratio = 10
# vm.dirty_ratio = 20
# vm.swappiness = 60
