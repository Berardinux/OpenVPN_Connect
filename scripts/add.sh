#!/bin/bash

if [ ! -d "/etc/openvpn/.ovpn" ]; then
    sudo mkdir /etc/openvpn/.ovpn
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
nu_switch=$(cat /opt/OpenVPN/OpenVPN | sed -n '2p' | cut -d '"' -f 2)
ln_switch=$(($(cat /opt/OpenVPN/OpenVPN | grep -n '"END" ///' | cut -d ':' -f 1) - 1))

read -r -d '' code_switch << EOM
        # Switch $nu_switch
        switch_with_label_button1 = self.create_switch_with_label_button("Label for Switch 1")
        switch_box.pack_start(switch_with_label_button1, False, False, 0)
EOM
#sudo awk -i inplace -v code="$code_switch" 'NR==$ln_switch {print code} 1' /opt/OpenVPN/OpenVPN