#!/bin/bash

if [ ! -d "/etc/openvpn/.ovpn" ]; then
    sudo mkdir /etc/openvpn/.ovpn
else
    sudo rm -r /etc/openvpn/.ovpn/*
fi
if [ $# -ne 1 ]; then
    echo "Usage: $0 <source_file>"
    exit 1
fi
selected_file_path="$1"
destination_path=/etc/openvpn/.ovpn
if [[ "$selected_file_path" == *.ovpn ]]; then
    sudo cp "$selected_file_path" "$destination_path"
else
    echo "Error: File does not have .ovpn extension."
    exit 1
fi
####################################################################################################

nu_switch=$(cat /opt/OpenVPN/OpenVPN | sed -n '2p' | cut -d '"' -f 2)
new_nu=$((nu_switch+1))
ln_switch=$(($(cat /opt/OpenVPN/OpenVPN | grep -n '"END" ///' | cut -d ':' -f 1) - 1))
ovpn_name=$(ls /etc/openvpn/.ovpn/)
name=$(echo "$ovpn_name" | cut -d "." -f 1)

if [ -f "/etc/openvpn/client/$ovpn_name" ]; then
    echo "$ovpn_name Is already used!"
    exit 1
else
    sudo mv /etc/openvpn/.ovpn/$ovpn_name /etc/openvpn/client
fi

if [ "$((nu_switch))" -le 8 ]; then
    read -r -d '' code_switch << EOM
        # Switch $nu_switch
            {
                "label": "$name vpn",
                "command_on": self.run_command_switch_on,
                "command_off": self.run_command_switch_off,
                "command_switch_on": ["pkexec", "bash", "/opt/OpenVPN/scripts/on.sh", "$name"],
                "command_switch_off": ["pkexec", "killall", "openvpn"],
            },
    
EOM
    sudo sed -i "s/##### --\"$nu_switch\"-- #####/##### --\"$new_nu\"-- #####/" "/opt/OpenVPN/OpenVPN"
    awk -v line="$ln_switch" -v code="$code_switch" 'NR==line{print code}1' /opt/OpenVPN/OpenVPN | sudo tee /opt/OpenVPN/OpenVPN >/dev/null
else
    echo "$nu_switch There are to many switchs"
    exit 1
fi

