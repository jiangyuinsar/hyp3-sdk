"""Errors and exceptions to raise when the SDK runs into problems"""


class ValidationError(Exception):
    """Raise when jobs do not pass validation"""


class AuthenticationError(Exception):
    """Raise when authentication does not succeed"""
