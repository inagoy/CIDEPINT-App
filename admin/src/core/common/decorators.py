from functools import wraps
from flask import abort, session
from src.core.models.user import User
from src.core.models.privileges import Role


class DecoratorManager:
    @classmethod
    def wrap_args(cls, *args_cls, **kwargs_cls):
        def decorator(func):
            @wraps(func)
            def decorator_function(*args, **kwargs):
                if not cls.evaluate(*args_cls, **kwargs_cls):
                    return cls.error_decorator(*args, **kwargs)
                return func(*args, **kwargs)
            return decorator_function
        return decorator

    @classmethod
    def wrap(cls, func):
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if not cls.evaluate(*args, **kwargs):
                return cls.error_decorator(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapped_func

    def evaluate_condition(*args, **kwargs) -> bool:
        return False

    def error(self, *args, **kwargs) -> bool:
        abort(401)

    @classmethod
    def evaluate(cls, *args, **kwargs) -> object:
        instance = cls()
        return instance.evaluate_condition(*args, **kwargs)

    @classmethod
    def error_decorator(cls, *args, **kwargs) -> bool:
        instance = cls()
        return instance.error(*args, **kwargs)


class LoginWrap(DecoratorManager):
    def evaluate_condition(*args, **kwargs):
        return session.get("user") is not None


class PermissionWrap(DecoratorManager):
    @classmethod
    def evaluate_condition(*args, **kwargs):
        if "permissions" not in kwargs:
            return False

        required_permissions = kwargs["permissions"]
        user = User.find_user_by_email(session["user"])

        institution = session.get("current_institution")

        role_id = (User.get_role_in_institution(user_id=user.id,
                                                institution_id=institution))

        if not role_id:
            return False

        response = Role.check_permissions(
                    role_id=role_id,
                    required_permissions=required_permissions)

        return response
