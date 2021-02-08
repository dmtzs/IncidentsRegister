#!/bin/bash
echo "===Initializing instalation of the configuration of the django server==="
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo ln -svf /usr/bin/python3 /usr/bin/python

echo "===Installing Nginx==="
sudo apt install nginx

echo "===Installing git==="
sudo apt install git

echo "===Installing virtual environment for django==="
sudo apt install python-virtualenv

#echo "===Creating system user==="
#sudo adduser --system --quiet --shelkl=/bin/bash --home=/home/django --gecos 'django' --group django
#gpasswd -a django sudo

echo "===Creating virtual environment==="
virtualenv /home/django/.venv --python=python3
source /home/django/.venv/bin/activate

echo "===Installing django==="
pip3 install django

echo "===Cloning the project from github==="
read -p "Enter the direction of the repo that you want to clone" gitrepo
git -C /home/django clone $gitrepo
#read -p "Enter the name of the father folder (django-father): " project
#p "Enter the name of the main app of django: " djapp

echo "===Installing dependencies==="
pip3 install -r /home/django/$project/requirements.txts