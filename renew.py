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

    # cleanup 脚本路径
    cleanup_path = os.path.join(
        os.path.split(os.path.realpath(__file__))[0],
        'cleanup.sh'
    )
    if not os.path.isfile(cleanup_path):
        logger.critical('Can not find cleanup.sh')
        raise FileNotFoundError(cleanup_path + ' not exist')

    # 多个域名
    for domain in domains:
        logger.info('Renew {} SSL certificate'.format(domain))
        # 设置环境变量
        os.environ['RENEW_DOMAIN'] = domain
        subprocess.call(
            '{} renew --cert-name {} --manual-auth-hook {} --manual-cleanup-hook {}'.format(
                certbot_path, domain, authenticator_path, cleanup_path
            ),
            shell=True
        )
