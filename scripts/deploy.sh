#!/bin/bash

docker network create user-service

DOCKER_PATH=docker-compose.yaml

docker-compose -f $DOCKER_PATH down &&\
	docker-compose -f $DOCKER_PATH build &&\
	docker-compose -f $DOCKER_PATH up -d
