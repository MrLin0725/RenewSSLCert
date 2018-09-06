import os
import time

from app.exceptions import NotFoundConfig
from app.tools.params import get_params

try:
    from config import Config
except ModuleNotFoundError:
    raise NotFoundConfig

if __name__ == '__main__':
    (certbot_dir, domains) = get_params('CERTBOT_DIR', 'DOMAINS')

    # certbot-auto 绝对路径
    certbot_path = os.path.join(certbot_dir, 'certbot-auto')
    if not os.path.isfile(certbot_path):
        raise FileNotFoundError('Can not found certbot-auto')

    # authenticator 脚本绝对路径
    authenticator_path = os.path.join(
        os.path.split(os.path.realpath(__file__))[0],
        'authenticator.sh'
    )
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
