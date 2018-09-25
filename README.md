# Let's Encrypt SSL证书自动续期

> 如果你的域名在腾讯云解析，可以使用这个小工具自动续期 Let's Encrypt 的SSL证书。

### 环境依赖
 - Linux
 - Python3
 - crontab

### 使用方法
> 根据需要使用虚拟环境
```bash
# 安装依赖
pip install -r requirements.txt

# 配置文件
cp config.example.py config.py
vim config.py

vim /etc/crontab
# 插入
0 0 1 * * root cd /path/RenewSSLCert && python renew.py
```
