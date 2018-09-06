import hmac
from base64 import b64encode
from hashlib import sha1

from app.exceptions import NotFoundConfig
from app.tools.params import get_params

try:
    from config import Config
except ModuleNotFoundError:
    raise NotFoundConfig


def sign(**params):
    """生成腾讯云接口需要的签名串

    Args:
        params (:obj:`dict`): 请求参数

    Attributes:
        api (str): 请求主机 +请求路径
        base_str (str): 原始字符串，请求方法 + 请求主机 +请求路径 + ? + 请求字符串

    Returns:
        str: 签名串
    """
    api = '/'.join([
        Config.TENCENT_CNS_API.strip('/'),
        Config.TENCENT_CNS_API_LOCATION.strip('/')
    ])

    (secret_key) = get_params('TENCENT_CNS_SECRETKEY')

    # 按照升序排列
    params_strings = '&'.join([
        '{}={}'.format(key, params[key]) for key in sorted(params)
    ])
    base_str = 'GET' + api + '?' + params_strings
    hashed = hmac.new(
        bytes(secret_key, encoding="utf-8"),
        bytes(base_str, encoding="utf-8"),
        sha1
    )

    return b64encode(hashed.digest()).decode('utf-8')
