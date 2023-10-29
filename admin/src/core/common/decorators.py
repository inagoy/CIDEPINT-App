"""Decorators."""
from functools import wraps
from flask import abort, session
from src.core.models.user import User
from src.core.models.privileges import Role
from src.core.models.site_config import SiteConfig
from src.core.controllers import site_config_controller


class DecoratorManager:
    """
    Base class for creating decorators.

    The decorators evaluate conditions before executing functions.
    """

    @classmethod
    def wrap_args(cls, *args_cls, **kwargs_cls):
        """
        Wrap a function and evaluates a class method before calling it.

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
        """
        Wrap a given function with classmethod decorator.

        Parameters:
            func: The function to be wrapped.

        Returns:
            The wrapped function.
        """
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if not cls.evaluate(*args, **kwargs):
                return cls.error_decorator(*args, **kwargs)
            return func(*args, **kwargs)

        return wrapped_func

    def evaluate_condition(*args, **kwargs) -> bool:
        """
        Evaluate a condition based on the arguments and keyword arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: The evaluated boolean value.
        """
        return False

    def error(self, *args, **kwargs) -> bool:
        """Return the error decorator."""
        abort(401)

    @classmethod
    def evaluate(cls, *args, **kwargs) -> object:
        """Return the evaluate condition."""
        instance = cls()
        return instance.evaluate_condition(*args, **kwargs)

    @classmethod
    def error_decorator(cls, *args, **kwargs) -> bool:
        """Return the error decorator."""
        instance = cls()
        return instance.error(*args, **kwargs)


class LoginWrap(DecoratorManager):
    """
    Login decorator.

    Checks if a user is authenticated before executing a function.
    """

    def evaluate_condition(*args, **kwargs):
        """Return True if a user is authenticated."""
        return session.get("user") is not None


class PermissionWrap(DecoratorManager):
    """
    User permissions decorator.

    Checks if the user has the specified permissions
    before executing a function.
    """

    @classmethod
    def evaluate_condition(*args, **kwargs):
        """
        Evaluate the condition based on the arguments and keyword arguments.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            bool: True if the condition is met, False otherwise.
        """
        if "permissions" not in kwargs:
            return False

        required_permissions = kwargs["permissions"]
        user = User.find_user_by(field='email', value=session["user"])

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
    Maintenace Mode check decorator.

    Checks if the site is not in maintenance mode
    before executing a function.
    """

    def error(self, *args, **kwargs) -> bool:
        """Return True if the site is currently in maintenance mode."""
        return site_config_controller.in_maintenance_mode()

    @classmethod
    def evaluate_condition(*args, **kwargs):
        """Return True if the site is not in maintenance mode."""
        return not SiteConfig.in_maintenance_mode()
