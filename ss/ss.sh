#!/bin/bash

yum -y install python-pip
pip install shadowsock
wget https://raw.githubusercontent.com/silenceshell/myscripts/master/ss/shadowsocks.json -O /etc/shadowsocks.json
ssserver -c /etc/shadowsocks.json -d start

wget https://raw.githubusercontent.com/silenceshell/myscripts/master/ss/shadowsocks.service -O /etc/systemd/system/shadowsocks.service
systemctl enable shadowsocks
systemctl start shadowsocks
systemctl status shadowsocks -l
