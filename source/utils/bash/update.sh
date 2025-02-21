#!/bin/bash

echo "Updating packages."

sudo apt update -y
sudo apt upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove -y

echo "Updating Python packages..."

python3 -m pip install --upgrade pip

pip3 freeze | cut -d = -f 1 | xargs -n1 pip3 install --upgrade

echo "All packages have been updated."
