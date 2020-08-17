#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/ /data/web_static/ /data/web_static/releases/ /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "keep quiet plz" | sudo tee /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "\\tlocation \/hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t" /etc/nginx/sites-enabled/default
sudo service nginx restart
