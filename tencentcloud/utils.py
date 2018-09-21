import os

from .exceptions import HandlerException

try:
    from config import Config
except ModuleNotFoundError as e:
    e.msg = '配置文件 {} 不存在'.format(
        os.path.join(
            os.path.split(os.path.realpath(__file__))[0],
            'config.py'
        )
    )
    raise


def get_params(*args):
    """通过Config获取参数值"""
    values = []
    for arg in args:
        try:
            values.append(getattr(Config, arg))
        except AttributeError:
            raise HandlerException('ConfigNotFound', arg)

    if len(values) > 1:
        return tuple(values)
    else:
        return values[0]
