import sys

from app.tencent.request import create_record

if __name__ == '__main__':
    # 获取 authenticator.sh 传递的三个参数：域名，子域名，记录值
    domain = sys.argv[1]
    sub_domain = sys.argv[2]
    value = sys.argv[3]

    # TODO: 获取解析记录，判断是否有已经存在的记录
    # TODO: 删除存在的记录

    # 创建解析记录
    create_record(domain=domain, sub_domain=sub_domain, value=value)
