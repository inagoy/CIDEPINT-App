from functools import wraps
from flask import abort, session
from src.core.models.user import User
from src.core.models.privileges import Role
from src.core.models.site_config import SiteConfig
from src.core.controllers import site_config_controller


class DecoratorManager:
    """
    Base class for creating decorators that evaluate conditions before
    executing functions.

    Attributes:
        None

    Methods:
        - wrap_args(cls, *args_cls, **kwargs_cls):
            A decorator that wraps a function and evaluates a class method
            before calling it. It accepts arguments and keyword arguments when
            decorating a function.

        - wrap(cls, func):
            A decorator that wraps a function and evaluates the class's
            condition before calling it.

        - evaluate_condition(*args, **kwargs):
            Subclasses should override this method. It evaluates a condition
            based on the provided arguments and keyword arguments and returns
            a boolean value.

        - error(self, *args, **kwargs):
            Subclasses can override this method. It defines the action to be
            taken if the condition evaluation fails.

        - evaluate(cls, *args, **kwargs):
            Creates an instance of the class and calls its evaluate_condition
            method with the provided arguments and keyword arguments.

        - error_decorator(cls, *args, **kwargs):
            Evaluates a condition and, if it fails, calls the error method of
            the class to handle the error.

    """

    @classmethod
    def wrap_args(cls, *args_cls, **kwargs_cls):
        """
        A decorator that wraps a function and evaluates a class
        method before calling it.

        Parameters:
            *args_cls (tuple): The arguments to evaluate the class method with.
            **kwargs_cls (dict): The keyword arguments to evaluate the
            class method with.

        Returns:
            function: The wrapped function that calls the class method and
             the original function.
        """
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
    """
    Decorator that checks if a user is authenticated before
    executing a function.
    """

    def evaluate_condition(*args, **kwargs):
        return session.get("user") is not None


class PermissionWrap(DecoratorManager):
    """
    Decorator that checks if the user has the specified permissions
    before executing a function.
    """

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


class MaintenanceWrap(DecoratorManager):
    """
    Decorator that checks if the site is not in maintenance mode
    before executing a function.
    """

    def error(self, *args, **kwargs) -> bool:
        return site_config_controller.in_maintenance_mode()

    @classmethod
    def evaluate_condition(*args, **kwargs):
        return not SiteConfig.in_maintenance_mode()
