#!/usr/bin/env bash

subDomain="_acme-challenge"

$(which python3) handler.py ${RENEW_DOMAIN} ${subDomain} ${CERTBOT_VALIDATION}
sleep 30
