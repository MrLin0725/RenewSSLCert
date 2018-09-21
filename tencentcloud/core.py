import hmac
import time
from base64 import b64encode
from hashlib import sha1
from random import randint

import requests

from tencentcloud.exceptions import HandlerException
from tencentcloud.logs import Logger
from tencentcloud.utils import get_params


class TencentCloudRequester(object):
    """请求腾讯云接口"""

    api = 'cns.api.qcloud.com/v2/index.php'
    request_api = 'https://' + api
    record_type = 'TXT'
    record_line = '默认'
    params = {}
    request_retry = 3

    def __init__(self, domain, sub_domain, value):
        self.domain = domain
        self.sub_domain = sub_domain
        self.value = value
        (self.secret_id, self.secret_key) = get_params('TENCENT_CNS_SECRETID', 'TENCENT_CNS_SECRETKEY')
        self.logger = Logger()
        self.logger.info('Initialization done...')

    def __sign(self):
        """生成腾讯云接口需要的签名串

        Returns:
            str: 签名串
        """
        params_strings = '&'.join([
            '{}={}'.format(key, self.params[key]) for key in sorted(self.params)
        ])
        base_str = 'GET' + self.api + '?' + params_strings
        hashed = hmac.new(
            bytes(self.secret_key, encoding="utf-8"),
            bytes(base_str, encoding="utf-8"),
            sha1
        )
        return b64encode(hashed.digest()).decode('utf-8')

    def __request(self):
        """请求"""
        self.logger.info('Request: {}'.format(self.request_api))
        for _ in range(self.request_retry):
            response = requests.get(self.request_api, params=self.params)
            if response.status_code == 200:
                self.logger.info('Request successfully...')
                return response.json()
        self.logger.error('Request failed...')
        return dict()

    def __gen_common_params(self, action):
        """生成公共参数"""
        return dict(
            Action=action,
            Timestamp=int(time.time()),
            Nonce=randint(10000, 99999),
            SecretId=self.secret_id
        )

    def create_record(self):
        """添加解析记录"""
        self.logger.info('Create DNS record start...')
        self.params = self.__gen_common_params(action='RecordCreate')
        self.params.update(
            dict(
                domain=self.domain,
                subDomain=self.sub_domain,
                value=self.value,
                recordType=self.record_type,
                recordLine=self.record_line,
            )
        )
        self.params['Signature'] = self.__sign()
        result = self.__request()
        if result['codeDesc'] != 'Success':
            self.logger.critical('Create DNS record failed...')
            raise HandlerException('CreateRecordError', result['message'])
        self.logger.info('Create DNS record successfully...')
