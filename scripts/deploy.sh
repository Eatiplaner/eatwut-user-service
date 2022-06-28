#!/bin/bash

DOCKER_PATH=docker-compose.yaml

docker-compose -f $DOCKER_PATH down &&\
	docker-compose -f $DOCKER_PATH pull &&\
	docker-compose -f $DOCKER_PATH up -d
