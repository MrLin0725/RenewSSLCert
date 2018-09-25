import sys

from tencentcloud.core import TencentCloudRequester

if __name__ == '__main__':
    # 获取 authenticator.sh 传递的三个参数：域名，子域名，记录值
    domain = sys.argv[1]
    sub_domain = sys.argv[2]
    value = sys.argv[3]

    # 创建解析记录
    requester = TencentCloudRequester(domain=domain, sub_domain=sub_domain, value=value)
    requester.create_record()
