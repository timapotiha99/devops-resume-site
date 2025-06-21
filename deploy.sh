#!/bin/bash
cd /home/ubuntu/my-app || exit
git pull origin main
docker compose down
docker compose up -d --build
