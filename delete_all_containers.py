#!/usr/bin/python
# coding=utf8

import docker

docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock', version="1.24")

# print docker_client.images()

containers = docker_client.containers.list(all=True)

# docker_client.containers.prune()
for c in containers:
    print c
    c.remove(force=True)
    # print c[u'Id']
    # docker_client.containers()

containers = docker_client.containers.list(all=True)
for c in containers:
    print c
