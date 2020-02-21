# Let's Encrypt SSL证书自动续期

> 如果你的域名在腾讯云解析，并且使用certbot-auto，就可以使用这个小工具自动续期 Let's Encrypt 的SSL证书。

### 环境依赖
 - Linux
 - Python3
 - crontab
 - Nginx
 - certbot-auto

### 使用方法
> 需要提前申请好[Let's Encrypt SSL证书](./SSLCertificate.md)
```bash
# 安装依赖
pip install -r requirements.txt

# 配置文件
cp config.example.py config.py
vim config.py

# 定时任务
vim /etc/crontab
0 0 1 * * root cd /path/RenewSSLCert && /path/python renew.py >> renew.log && /bin/systemctl nginx restart
```
