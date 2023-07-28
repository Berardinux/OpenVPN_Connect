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
new_nu=$((nu_switch+1))
ln_switch=$(($(cat /opt/OpenVPN/OpenVPN | grep -n '"END" ///' | cut -d ':' -f 1) - 1))

if [ "$nu_switch" -le 8 ]; then
    read -r -d '' code_switch << EOM
        # Switch $nu_switch
        switch_with_label_button$nu_switch = self.create_switch_with_label_button("Label for Switch 1")
        switch_box.pack_start(switch_with_label_button$nu_switch, False, False, 0)
    
EOM
    sudo sed -i "s/##### --\"$nu_switch\"-- #####/##### --\"$new_nu\"-- #####/" "/opt/OpenVPN/OpenVPN"
    awk -v line="$ln_switch" -v code="$code_switch" 'NR==line{print code}1' /opt/OpenVPN/OpenVPN | sudo tee /opt/OpenVPN/OpenVPN >/dev/null
else
    echo "$nu_switchs Switchs is the limit"
fi