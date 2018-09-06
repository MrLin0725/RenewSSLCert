from app.exceptions import ConfigValueError, NotFoundConfig

try:
    from config import Config
except ModuleNotFoundError:
    raise NotFoundConfig


def get_params(*args):
    """获取参数"""

    values = []
    for arg in args:
        try:
            values.append(getattr(Config, arg))
        except AttributeError:
            raise ConfigValueError(arg)

    if len(values) > 1:
        return tuple(values)
    else:
        return values[0]
