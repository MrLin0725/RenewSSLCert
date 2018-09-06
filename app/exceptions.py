class ConfigValueError(Exception):
    """参数错误"""

    def __init__(self, config_name=None):
        super(ConfigValueError, self).__init__(config_name)
        self.config_name = config_name

    def __str__(self):
        if self.config_name:
            return self.config_name
        else:
            return 'Missing configuration, please check'


class NotFoundConfig(Exception):
    """找不到配置文件"""

    def __init__(self):
        super(NotFoundConfig, self).__init__()

    def __str__(self):
        return 'Can not found configuration file `config.py`'


class RequestError(Exception):
    """请求错误"""

    def __init__(self):
        super(RequestError, self).__init__()

    def __str__(self):
        return 'Request failed'


class CreateRecordError(Exception):
    """添加解析出错"""

    def __init__(self, code, msg):
        super(CreateRecordError, self).__init__(code, msg)
        self.code = code
        self.msg = msg

    def __str__(self):
        return 'Create record failed: [{}] {}'.format(self.code, self.msg)
