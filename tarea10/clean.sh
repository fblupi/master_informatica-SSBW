#!/bin/sh

sudo docker stop restaurantator_db
sudo docker stop restaurantator_app
sudo docker stop restaurantator_nginx
sudo docker rm restaurantator_db
sudo docker rm restaurantator_app
sudo docker rm restaurantator_nginx
sudo docker rmi restaurantator_db_img
sudo docker rmi restaurantator_app_img
sudo docker rmi restaurantator_nginx_img
