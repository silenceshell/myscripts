#!/bin/bash

#like: gcr.io/google_containers/echoserver:1.8
#$1 should be echoserver:1.8
docker pull anjia0532/$1
docker tag anjia0532/$1 docker.example.com:8117/google_containers/$1
docker push docker.example.com:8117/google_containers/$1
docker rmi docker.example.com:8117/google_containers/$1
docker rmi anjia0532/$1


