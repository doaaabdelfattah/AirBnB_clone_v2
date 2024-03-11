#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Install Nginx
apt-get update
apt-get install -y nginx

# Create directorirs & files
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Holberton School" > /data/web_static/releases/test/index.html

# Create the symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change Permissions
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# NGINX Config File
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;

    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}

" > /etc/nginx/sites-available/default


# Restart server
service nginx restart