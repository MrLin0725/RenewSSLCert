import sys

from app.tencent.request import create_record

if __name__ == '__main__':
    # 获取 authenticator.sh 传递的三个参数：域名，子域名，记录值
    create_record(domain=sys.argv[1], sub_domain=sys.argv[2], value=sys.argv[3])
