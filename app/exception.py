class UserNotFoundException(Exception):
    detail = "User not fount"


class UserNotCorrectPasswordException(Exception):
    detail = "Please check you'r login or password an correct"


class HasNotPermission(Exception):
    detail = "You'r has't permission for this operation"

class TokenNotCorrect(Exception):
    detail = "Token not correct"

class TokenExpired(Exception):
    detail = "Token is expired"

class RoleNotFoundException(Exception):
    detail = "Role not found or you'r not permission for this operation"
