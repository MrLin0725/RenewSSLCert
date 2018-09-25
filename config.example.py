import os


class Config(object):
    """参数设置"""

    # 需要续期的域名
    DOMAINS = [
        'example1.com',
        'example2.com',
    ]
    # certbot-auto 目录绝对路径
    CERTBOT_DIR = '/root'
    # 是否需要测试
    CERTBOT_TEST = True

    # 腾讯云解析 SecretId
    TENCENT_CNS_SECRETID = ''
    # 腾讯云解析 SecretKey
    TENCENT_CNS_SECRETKEY = ''

    # 日志路径
    LOG_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'renew.log')
