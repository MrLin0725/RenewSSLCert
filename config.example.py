class Config(object):
    """参数设置"""

    # 需要续期的域名
    DOMAINS = [
        'example1.com',
        'example2.com',
    ]
    # certbot-auto 目录绝对路径
    CERTBOT_DIR = '/root'

    # 腾讯云解析API地址
    TENCENT_CNS_API = 'cns.api.qcloud.com'
    # 腾讯云解析API路径
    TENCENT_CNS_API_LOCATION = '/v2/index.php'
    # 腾讯云解析 Action Name
    TENCENT_CNS_ACTION_NAME = 'RecordCreate'
    # 腾讯云解析 SecretId
    TENCENT_CNS_SECRETID = ''
    # 腾讯云解析 SecretKey
    TENCENT_CNS_SECRETKEY = ''
