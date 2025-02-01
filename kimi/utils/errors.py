class ValidationError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class TokenExpiredError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)


class AuthenticationError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)
