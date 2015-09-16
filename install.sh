#!/bin/bash

bylistart="$(tput bold)"
byliend="$(tput rmso)$(tput dim)"
echo "${bylistart} \n Ubuntu-AutoSuspend Install \n ${byliend}";
echo "${bylistart} \n Updating and Upgrading... ${byliend}"
sudo apt-get update;
sudo apt-get -y upgrade;
echo "${bylistart} Installing bluez pip and git-core... ${byliend}"
sudo apt-get -y install bluez pip git-core;
cd ~;
echo "${bylistart}\n Installing bluez-python...\n ${byliend}";
pip install pybluez

echo "${bylistart}\n Downloading Ubuntu-AutoSuspend...\n ${byliend}";
git clone https://github.com/csicar/Ubuntu-AutoSuspend Ubuntu-AutoSuspend
cd Ubuntu-AutoSuspend

echo " ${bylistart} Enter the Mac-Address form your phone: ${byliend}"
read MAC </dev/tty

LINE=" $(pwd)/script.py ${MAC} &"
echo $LINE | sudo tee --append /etc/init.d/rc.local

tput sgr0

