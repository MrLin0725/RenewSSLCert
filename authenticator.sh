#!/usr/bin/env bash

subDomain="_acme-challenge"

# 通过环境变量 RENEW_DOMAIN 获取需要续期的域名
# CERTBOT_VALIDATION 是certbot设置的变量
$(which python3) handler.py ${RENEW_DOMAIN} ${subDomain} ${CERTBOT_VALIDATION}

# 等待DNS解析生效
sleep 30
