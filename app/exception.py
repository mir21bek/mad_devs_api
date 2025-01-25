class UserNotFoundException(Exception):
    detail = "User not fount"

class UserNotCorrectPasswordOrLogin(Exception):
    detail = "Please check you'r login or password an correct"


class HasNotPermission(Exception):
    detail = "You'r has't permission for this operation"
