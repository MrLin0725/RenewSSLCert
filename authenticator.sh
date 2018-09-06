#!/usr/bin/env bash

subDomain="_acme-challenge"

$(which python3) run.py ${RENEW_DOMAIN} ${subDomain} ${CERTBOT_VALIDATION}
