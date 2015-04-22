#!/bin/bash

echo "Install required packages"

echo "Update the system"
apt-get update

echo "Install Python 2.7 and setuptools"
apt-get install -y python2.7-dev python-setuptools

echo "Install pip"
easy_install pip

echo "Install Python modules"
pip install -r requirements.txt

echo "Install wget"
apt-get install wget

echo "Install curl"
apt-get install curl



