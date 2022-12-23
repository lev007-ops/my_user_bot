#!/bin/bash

echo Stopping my-user-bot-container
docker stop my-user-bot-container

echo Pulling data from git
git pull

echo Build my-user-bot image
docker build --tag my-user-bot .

echo Start my-user-bot-container
docker run -d --rm --name my-user-bot-container  my-user-bot