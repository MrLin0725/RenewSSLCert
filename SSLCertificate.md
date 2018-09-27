# Let's Encrypt 申请SSL证书


---


### 运行环境
- OS: `Ubuntu 16.04`


### 必要的准备
- `Nginx`

- `certbot-auto`

- 域名 `example.com` _根据实际情况修改_


### 证书保存的路径
- `/etc/letsencrypt/live/example.com`


### 证书申请

1. 下载 `certbot-auto`
```bash
wget https://dl.eff.org/certbot-auto
```

2. 设置可执行权限
```bash
chmod a+x certbot-auto
```

3. <p id="apply">证书申请</p>
```bash
./certbot-auto certonly -d "*.example.com" --manual --preferred-challenges dns --server https://acme-v02.api.letsencrypt.org/directory
```

4. 输入邮箱，用于安全提醒以及续期提醒
```
 Saving debug log to /var/log/letsencrypt/letsencrypt.log
 Plugins selected: Authenticator manual, Installer None
 Enter email address (used for urgent renewal and security notices)
  (Enter 'c' to cancel): your@mail.com
```

5. 同意 `Let's Encrypt` 协议要求，输入 `A`
```
 Please read the Terms of Service at
 https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
 agree in order to register with the ACME server at
 https://acme-v02.api.letsencrypt.org/directory
 --------------------------------------------------------
 (A)gree/(C)ancel: A
```

6. 绑定域名和IP，输入 `Y`
```
 Are you OK with your IP being logged?
 --------------------------------------------------------
 (Y)es/(N)o: Y
```

7. 配置 DNS TXT记录
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

8. 确认 TXT 记录是否生效
```bash
 dig  -t txt  _acme-challenge.example.com @8.8.8.8
```

9. 校验证书信息
```bash
 openssl x509 -in  /etc/letsencrypt/live/example.com/cert.pem
```

10. 证书续期（阿里云、腾讯云等）

 同[证书申请](#apply)命令，需要手动添加DNS解析记录
