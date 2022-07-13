from typing import Optional


def greet(first_name: Optional[str] = None, last_name: Optional[str] = None):
    """
    Prepare a greeting message for a user

    Parameters
    ----------
    first_name : str
        The user's first name, or None if not available
    last_name : str
        The user's last name, or None if not available

    Returns
    -------
    str
        A personalised greeting for the user
    """
    return "Hello" + first_name + last_name
