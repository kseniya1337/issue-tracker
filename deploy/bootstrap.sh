#!/bin/bash

set -e

ssh root@issue-tracker.fletcher.pro bash -c '
  set -e
  apt-get update
  apt-get install -y socat apt-transport-https ca-certificates curl gnupg-agent software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
  add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  apt-get update
  apt-get install -y docker-ce docker-ce-cli containerd.io
  [ ! -d .acme.sh ] && curl https://get.acme.sh | sh
  ./.acme.sh/acme.sh --issue --standalone -d issue-tracker.fletcher.pro --force
  mkdir -p certs/
  ./.acme.sh/acme.sh --install-cert -d issue-tracker.fletcher.pro --cert-file certs/cert.pem --key-file certs/key.pem --fullchain-file certs/fullchain.pem
  mkdir -p acme-challenges/
'

[ -z $(docker-machine ls --filter 'NAME=issue-tracker.fletcher.pro' -q) ] && docker-machine create --driver generic --generic-ip-address=issue-tracker.fletcher.pro --generic-ssh-user=root --generic-ssh-key ~/.ssh/id_rsa issue-tracker.fletcher.pro

./deploy/deploy.sh

ssh root@issue-tracker.fletcher.pro bash -c '
  set -e
  ./.acme.sh/acme.sh --remove -d issue-tracker.fletcher.pro
  mkdir -p acme-challenges/
  ./.acme.sh/acme.sh --issue -d issue-tracker.fletcher.pro -w acme-challenges/
'
