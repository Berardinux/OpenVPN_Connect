#!/bin/bash

name="$1"

sudo openvpn /etc/openvpn/client/$name.ovpn > /opt/OpenVPN/config/vpn.log