import os
import subprocess

from tencentcloud.utils import get_params
from tencentcloud.logs import Logger

if __name__ == '__main__':
    logger = Logger()

    (certbot_dir, domains) = get_params('CERTBOT_DIR', 'DOMAINS')

    # certbot-auto 绝对路径
    certbot_path = os.path.join(certbot_dir, 'certbot-auto')
    if not os.path.isfile(certbot_path):
        logger.critical('Can not find certbot')
        raise FileNotFoundError(certbot_path + ' not exist')

    # authenticator 脚本绝对路径
    authenticator_path = os.path.join(
        os.path.split(os.path.realpath(__file__))[0],
        'authenticator.sh'
    )
    if not os.path.isfile(authenticator_path):
        logger.critical('Can not find authenticator.sh')
        raise FileNotFoundError(authenticator_path + ' not exist')

    # 多个域名
    for domain in domains:
        logger.info('Renew {} SSL certificate'.format(domain))
        # 设置环境变量
        os.environ['RENEW_DOMAIN'] = domain
        # FIXME: --dry-run 测试阶段
        subprocess.call(
            '{} renew --cert-name {} --manual-auth-hook {} --dry-run'.format(
                certbot_path, domain, authenticator_path
            ),
            shell=True
        )
