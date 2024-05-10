#!/bin/bash
#This is a simple script to build the docker image


echo "Initiating deployment"

echo "Pulling changes..."

git pull

echo "Building docker image..."

docker compose build

echo "Bringing up containers..."

docker compose up -d

echo "Deployment finished succesfully!"