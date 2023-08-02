#!/bin/bash

clear
distro=$(grep -w "NAME" /etc/os-release | cut -d= -f2 | tr -d '"' | cut -d' ' -f1)

if [ "$(id -u)" -ne 0 ]; then
	echo "Please run the script with sudo or as root"
	exit 1
else
	current_user=$SUDO_USER
fi	

if [ "$distro" = "Debian" ] || [ "$distro" = "Ubuntu" ]; then
    if dpkg -l | grep -q "openvpn"; then
        echo "openvpn is aready installed on your system already"
        sudo chmod 777 scripts/Uninstall.sh
	    sudo ./scripts/Uninstall.sh
	    exit 1
    else
        echo "OpenVPN is Not installed on your system yet"
    fi
elif [ "$distro" = "Arch" ]; then
    if pacman -Q openvpn >/dev/null 2>&1; then
        echo "OpenVPN is installed on your system already"
	    sudo chmod 777 scripts/Uninstall.sh
        sudo ./scripts/Uninstall.sh
	    exit 1
    else
        echo "OpenVPN is Not installed on your system yet"
    fi
else
    echo "Your Distro can not be installed using this install script sorry!"
    echo "Distros that can be installed include (Debian / Ubuntu / Arch)"
    exit 1
fi

clear

echo "# Are you ready to install OpenVPN? (Y/n) #"
read -r install
clear

echo "# Would you like to install the OpenVPN Connect? (Y/n)"
read -r app
clear

if [ -z $install ]; then
    install=Y
    if [ "$install" = "Y" ]; then
        if [ "$distro" = "Debian" ] || [ "$distro" = "Ubuntu" ]; then
            sudo apt update && sudo apt upgrade -y && sudo apt install openvpn -y
        elif [ "$distro" = "Arch" ]; then
            sudo pacman -Syu && sudo pacman -S --noconfirm openvpn
        else
            exit
        fi
    fi
else
    echo "# Okay, run the script again when you are ready to install! #"
    exit
fi

sudo mkdir -p /opt/OpenVPN
sudo cp -r * /opt/OpenVPN
touch "/home/$current_user/.local/share/applications/OpenVPN.desktop"
sudo chmod -R 777 /opt/OpenVPN/
chmod 777 "/home/$current_user/.local/share/applications/OpenVPN.desktop"

cat << EOM | sudo tee -a "/home/$current_user/.local/share/applications/OpenVPN.desktop" >/dev/null
[Desktop Entry]
Type=Application
Name=OpenVPN
Comment=OpenVPN
Icon=/opt/OpenVPN/Images/openvpn.png
Exec=/opt/OpenVPN/OpenVPN
Terminal=false
EOM

echo "###### Installation complete! ######"