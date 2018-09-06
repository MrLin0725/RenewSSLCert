import os
import time

from app.exceptions import ConfigValueError
from config import Config

if __name__ == '__main__':
    try:
        certbot_dir = Config.CERTBOT_DIR
    except AttributeError:
        raise ConfigValueError('CERTBOT_DIR')

    try:
        domains = Config.DOMAINS
    except AttributeError:
        raise ConfigValueError('DOMAINS')

    # certbot-auto 绝对路径
    certbot_path = os.path.join(certbot_dir, 'certbot-auto')
    if not os.path.isfile(certbot_path):
        raise FileNotFoundError('Can not found certbot-auto')

    # authenticator 脚本绝对路径
    authenticator_path = os.path.join(os.path.abspath('.'), 'authenticator.sh')
    if not os.path.isfile(authenticator_path):
        raise FileNotFoundError('Can not found authenticator.sh')

    # 多个域名
    for domain in domains:
        # 设置环境变量
        os.environ['RENEW_DOMAIN'] = domain
        # FIXME: --dry-run 测试阶段
        os.system(
            '{} renew --cert-name {} --manual-auth-hook {} --dry-run'.format(
                certbot_path, domain, authenticator_path
            )
        )
        # 腾讯云接口调用时间限制
        time.sleep(30)

    try:
        # 删除环境变量
        del os.environ['RENEW_DOMAIN']
    except KeyError:
        pass
