#!/bin/bash

sudo apt-get install git -y

sudo apt update && sudo apt upgrade

sudo apt install python3-pip

sudo apt-get install python3-pandas

pip install requests

echo 'clear' >> ~/.bashrc

echo 'sudo python3 ~/cheap_flights_raspberry_zero/main.py' >> ~/.bashrc

sudo reboot
