import time
from random import randint

import requests

from app.exceptions import ConfigValueError, RequestError, CreateRecordError
from app.tencent.signature import sign
from config import Config


def create_record(domain, sub_domain, value, record_type='TXT', record_line='默认'):
    """添加腾讯云解析记录

    Args:
        domain (:obj:`str`): 要添加解析记录的域名（主域名，不包括 www，例如：qcloud.com）
        sub_domain (:obj:`str`): 子域名，例如：www
        value (:obj:`str`): 记录值
        record_type (:obj:`str`, optional): 记录类型，默认值 `TXT`
        record_line (:obj:`str`, optional): 记录的线路名称，默认值 `默认`
    """
    # 腾讯云添加解析完整API路径
    cns_api = 'https://' + Config.TENCENT_CNS_API.strip('/') + '/' + Config.TENCENT_CNS_API_LOCATION.strip('/')
    # 当前时间戳
    timestamp = int(time.time())
    # 随机正整数
    nonce = randint(10000, 99999)

    try:
        # Action Name
        action = Config.TENCENT_CNS_ACTION_NAME
    except AttributeError:
        raise ConfigValueError('TENCENT_CNS_ACTION_NAME')

    try:
        # SecretId
        secret_id = Config.TENCENT_CNS_SECRETID
    except AttributeError:
        raise ConfigValueError('TENCENT_CNS_SECRETID')

    params = dict(
        Action=action,
        Timestamp=timestamp,
        Nonce=nonce,
        SecretId=secret_id,
        domain=domain,
        subDomain=sub_domain,
        value=value,
        recordType=record_type,
        recordLine=record_line,
    )
    # 添加签名参数
    params['Signature'] = sign(**params)

    # 请求
    response = requests.get(cns_api, params=params)
    if response.status_code != 200:
        raise RequestError

    result = response.json()
    if result['codeDesc'] != 'Success':
        raise CreateRecordError(result['code'], result['message'])
