#!/bin/bash
echo "INSTALL SCRIPT"
cd ~/
echo "Installing git"
sudo apt update
sudo apt install git
git --version
git config --global user.name "Mayank Thakur"
git config --global user.email "thakurmayank88@gmail.com"
echo "Git done"
echo "Installing DOCKER"
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose
sudo docker run hello-world
echo "Installed docker"
echo "Generating keys"
ssh-keygen -t rsa -b 4096 -C "thakurmayank88@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
echo "COPY BELOW"
cat ~/.ssh/id_rsa.pub
