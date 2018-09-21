class HandlerException(Exception):

    def __init__(self, error_type=None, message=None):
        self.error_type = error_type
        self.message = message

    def __str__(self):
        return '[{}]: {}'.format(self.error_type, self.message)
