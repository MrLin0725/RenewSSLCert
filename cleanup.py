import sys

from tencentcloud.core import TencentCloudRequester

if __name__ == '__main__':
    # 获取 cleanup.sh 传递的两个参数：域名，子域名
    domain = sys.argv[1]
    sub_domain = sys.argv[2]

    # 创建解析记录
    requester = TencentCloudRequester(domain=domain, sub_domain=sub_domain)
    requester.delete_record()
