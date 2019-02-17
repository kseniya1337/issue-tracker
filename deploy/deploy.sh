#!/bin/bash

set -e

eval $(docker-machine env issue-tracker.fletcher.pro)

docker-compose up --build -d
