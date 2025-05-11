#!/bin/bash

name=$1
start=$(cat /opt/OpenVPN/OpenVPN | grep -n '{"'$name'"}' | cut -d ':' -f 1)
end=$((start + 8))
nu=$(cat /opt/OpenVPN/OpenVPN | sed -n '2p' | cut -d '"' -f 2)
new_nu=$((nu-1))

echo "Name: $name"
echo "Start line: $start"
echo "End line: $end"

if [ "$nu" -ge 1 ]; then
    sudo sed -i "${start},${end}d" /opt/OpenVPN/OpenVPN
    sudo sed -i "s/##### --{\"$nu\"}-- #####/##### --{\"$new_nu\"}-- #####/" "/opt/OpenVPN/OpenVPN"
    sudo rm /etc/openvpn/client/$name.ovpn
fi