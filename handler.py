import sys

from app.tencent.request import create_record

if __name__ == '__main__':
    create_record(domain=sys.argv[1], sub_domain=sys.argv[2], value=sys.argv[3])
