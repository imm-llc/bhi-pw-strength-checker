#!/usr/bin/env bash

if [ "$UID" != 0 ]
then
echo "Please run as root"
exit 1
fi

echo "Installing Packages"
echo "==============================="
yum -y install nginx python36 python36-devel python36-setuptools 1>/dev/null

echo "Setting up service and config files"
echo "===================================="

cp service/bhipwc.conf /etc/httpd/nginx/conf.d/
cp service/bhipwc.servce /etc/systemd/system/

systemctl daemon-reload
systemctl enable bhipwc
systemctl start bhipwc

systemctl enable nginx
systemctl start nginx
