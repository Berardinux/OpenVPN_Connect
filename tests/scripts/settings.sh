#!/bin/bash

settings=$1

rm /opt/OpenVPN/Images/*.png
rm /opt/OpenVPN/Images/*.jpeg

case "$settings" in
    dark)
        echo "dark"
        cp /opt/OpenVPN/Images/Dark/* /opt/OpenVPN/Images
        sed -i 's/color: black;/color: white;/g' /opt/OpenVPN/styles.css
        ;;
    light)
        echo "light"
        cp /opt/OpenVPN/Images/Light/* /opt/OpenVPN/Images
        sed -i 's/color: white;/color: black;/g' /opt/OpenVPN/styles.css
        ;;
    *)
        echo "That is not a option )-:"
        ;;
esac