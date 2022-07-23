class BaseBlogException(Exception):
    ...


class UserAlreadyExists(BaseBlogException):
    ...


class UserNotFound(BaseBlogException):
    ...


class NotAuthorizedException(BaseBlogException):
    ...
