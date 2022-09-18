#!/usr/bin/env bash
<<<<<<< HEAD
# Prepare your web servers

## Update server
sudo apt-get -y update
sudo apt-get -y upgrade

## Install NGINX
sudo apt-get -y install nginx

## Creates directories
sudo mkdir -p /data/web_static/shared /data/web_static/releases/test

## Write Hello World in index with tee command
echo "Hello World" | sudo tee /data/web_static/releases/test/index.html

## Create Symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

## Change owner and group like ubuntu
sudo chown -R ubuntu:ubuntu /data

## Add new configuration to NGINX
sudo sed -i "/listen 80 default_server;/ a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

## Restart NGINX
sudo service nginx restart
=======
# sets up your web servers for the deployment of web_static

#install nginx web server 
apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Release test" >> /data/web_static/releases/test/index.html
# Create symlink, override if already exists
ln -sfn /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/ 

# Add static location to nginx settings: 

printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html;
        
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
}" > /etc/nginx/sites-available/default

service nginx restart
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
