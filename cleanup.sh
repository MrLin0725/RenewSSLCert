#!/usr/bin/env bash

subDomain="_acme-challenge"

# 通过环境变量 RENEW_DOMAIN 获取需要清理记录的域名
$(which python3) cleanup.py ${RENEW_DOMAIN} ${subDomain}