#!/bin/bash

echo "Initializing system"

# go
wget https://go.dev/dl/go1.23.7.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.23.7.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
go version

sudo chmod 666 /dev/kvm

mkdir -p ~/code/
cd ~/code/

git clone https://github.com/bookpanda/microvm-networking.git