"""
This module provides errors/exceptions and warnings of general use.

Exceptions that are specific to a given package should **not** be here,
but rather in the particular package.

This code is based on that provided by SunPy see
    licenses/SUNPY.rst
"""
import warnings

__all__ = [
    "{{cookiecutter.instr_name}}Warning",
    "{{cookiecutter.instr_name}}UserWarning",
    "{{cookiecutter.instr_name}}DeprecationWarning",
    "{{cookiecutter.instr_name}}PendingDeprecationWarning",
    "warn_user",
    "warn_deprecated",
]


class {{cookiecutter.instr_name}}Warning(Warning):
    """
    The base warning class from which all {{ cookiecutter.__short_string_name }} warnings should inherit.

    Any warning inheriting from this class is handled by the {{ cookiecutter.__short_string_name }}
    logger. This warning should not be issued in normal code. Use
    "{{cookiecutter.instr_name}}UserWarning" instead or a specific sub-class.
    """


class {{cookiecutter.instr_name}}UserWarning(UserWarning, {{cookiecutter.instr_name}}Warning):
    """
    The primary warning class for {{ cookiecutter.__short_string_name }}.

    Use this if you do not need a specific type of warning.
    """


class {{cookiecutter.instr_name}}DeprecationWarning(FutureWarning, {{cookiecutter.instr_name}}Warning):
    """
    A warning class to indicate a deprecated feature.
    """


class {{cookiecutter.instr_name}}PendingDeprecationWarning(PendingDeprecationWarning, {{cookiecutter.instr_name}}Warning):
    """
    A warning class to indicate a soon-to-be deprecated feature.
    """


def warn_user(msg, stacklevel=1):
    """
    Raise a `{{cookiecutter.instr_name}}UserWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, {{cookiecutter.instr_name}}UserWarning, stacklevel + 1)


def warn_deprecated(msg, stacklevel=1):
    """
    Raise a `{{cookiecutter.instr_name}}DeprecationWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, {{cookiecutter.instr_name}}DeprecationWarning, stacklevel + 1)
