# Let's Encrypt 申请SSL证书


---


### 运行环境
- OS: `Ubuntu 18.04`


### 必要的准备
- `Nginx`

- `certbot`

- 域名 `example.com` _根据实际情况修改_


### 证书保存的路径
- `/etc/letsencrypt/live/example.com`


### 证书申请

1. 下载安装 `certbot`
```bash
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot python-certbot-nginx
```

2. <p id="apply">证书申请</p>
```bash
certbot certonly -d "*.example.com" --manual --preferred-challenges dns --server https://acme-v02.api.letsencrypt.org/directory
```

3. 输入邮箱，用于安全提醒以及续期提醒
```
 Saving debug log to /var/log/letsencrypt/letsencrypt.log
 Plugins selected: Authenticator manual, Installer None
 Enter email address (used for urgent renewal and security notices)
  (Enter 'c' to cancel): your@mail.com
```

4. 同意 `Let's Encrypt` 协议要求，输入 `A`
```
 Please read the Terms of Service at
 https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
 agree in order to register with the ACME server at
 https://acme-v02.api.letsencrypt.org/directory
 --------------------------------------------------------
 (A)gree/(C)ancel: A
```

5. 绑定域名和IP，输入 `Y`
```
 Are you OK with your IP being logged?
 --------------------------------------------------------
 (Y)es/(N)o: Y
```

6. 配置 DNS TXT记录
```
 Please deploy a DNS TXT record under the name
 _acme-challenge.example.com with the following value:
 2_8KBE_jXH8nYZ2unEViIbW52LhIqxkg6i9mcwsRvhQ
 Before continuing, verify the record is deployed.
 --------------------------------------------------------
 Press Enter to Continue
```

 先在添加 `域名解析` 中添加解析记录：
 - 主机记录: \_acme-challenge
 - 记录类型: TXT
 - 记录值: *根据实际值填写*

 <br>

 添加完成后，按 `回车` 确认

7. 确认 TXT 记录是否生效
```bash
 dig  -t txt  _acme-challenge.example.com @8.8.8.8
```

8. 校验证书信息
```bash
 openssl x509 -in  /etc/letsencrypt/live/example.com/cert.pem
```
