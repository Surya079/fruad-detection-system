#!/bin/bash

echo "Stopping running containers"
docker stop $(docker ps -q)

echo  "Removing stopped containers.."
docker containers prune -f

echo "Removing unused images.."
docker images prune  -f

echo "Removing unused networks.."
docker networks prune -f 

echo "Docker cleanup finished.."

