#!/bin/sh

sudo docker build -t restaurantator_db_img db/
sudo docker run -d --name restaurantator_db restaurantator_db_img
sudo docker build -t restaurantator_app_img app/
sudo docker run -d --name restaurantator_app --link restaurantator_db restaurantator_app_img
sudo docker build -t restaurantator_nginx_img nginx/
sudo docker run -d --name restaurantator_nginx --link restaurantator_app -p 80:80 restaurantator_nginx_img
