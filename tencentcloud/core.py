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

    def __init__(self, domain, sub_domain='_acme-challenge', value=None):
        self.domain = domain
        self.sub_domain = sub_domain
        self.value = value
        (self.secret_id, self.secret_key) = get_params('TENCENT_CNS_SECRETID', 'TENCENT_CNS_SECRETKEY')
        self.logger = Logger()

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
        # 获取签名
        self.params['Signature'] = self.__sign()
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
        result = self.__request()
        if result['codeDesc'] != 'Success':
            self.logger.critical('Create DNS record failed...')
            raise HandlerException('CreateRecordError', result['message'])
        self.logger.info('Create DNS record successfully...')
        # 等待解析记录生效
        time.sleep(30)

    def list_record(self):
        """获取解析记录"""
        self.logger.info('Get DNS record start...')
        self.params = self.__gen_common_params(action='RecordList')
        self.params.update(
            dict(
                domain=self.domain,
                subDomain=self.sub_domain,
                recordType=self.record_type,
            )
        )
        result = self.__request()
        if result['codeDesc'] != 'Success':
            self.logger.error('Get DNS record failed...')
            return list()

        self.logger.info('Get DNS record successfully...')
        return result['data']['records']

    def delete_record(self):
        """删除解析记录"""
        self.logger.info('Clear DNS record start...')
        records = self.list_record()
        if not records:
            self.logger.info('DNS record is empty...')
        else:
            for record in records:
                self.params = self.__gen_common_params(action='RecordDelete')
                self.params.update(
                    dict(
                        domain=self.domain,
                        recordId=record['id']
                    )
                )
                result = self.__request()
                if result['codeDesc'] != 'Success':
                    self.logger.error('Delete DNS record {} failed...'.format(record['id']))
                else:
                    self.logger.info('Delete DNS record {} successfully...'.format(record['id']))
            self.logger.info('Clear DNS record completed...')
