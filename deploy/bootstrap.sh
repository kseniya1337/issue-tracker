#!/bin/bash

set -e

ssh root@issue-tracker.fletcher.pro bash -c '
  set -e
  apt-get update
  apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  apt-get update
  apt-get install -y docker-ce docker-ce-cli containerd.io
  mkdir -p media
'

[ -z $(docker-machine ls --filter 'NAME=issue-tracker.fletcher.pro' -q) ] && docker-machine create --driver generic --generic-ip-address=issue-tracker.fletcher.pro --generic-ssh-user=root --generic-ssh-key ~/.ssh/id_rsa issue-tracker.fletcher.pro

./deploy/deploy.sh
