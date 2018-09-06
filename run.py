import sys

from app.tencent.request import create_record

if __name__ == '__main__':
    create_record(domain=sys.argv[0], sub_domain=sys.argv[1], value=sys.argv[2])
    print('[Done]')
