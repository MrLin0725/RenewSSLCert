import os


class Config(object):
    """参数设置"""

    # 需要续期的域名
    DOMAINS = [
        'example1.com',
        'example2.com',
    ]
    # 测试模式：True or False
    CERTBOT_TEST = True

    # 腾讯云 SecretId
    TENCENT_CNS_SECRETID = ''
    # 腾讯云 SecretKey
    TENCENT_CNS_SECRETKEY = ''

    # 日志路径
    LOG_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'renew.log')
