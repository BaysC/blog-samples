from typing import Tuple


def clean_telephone_number(s: str) -> Tuple[str, str, str]:
    """
    Clean a telephone number, returning country code, area code, main number

    Parameters
    ----------
    s : str
        Input telephone

    Returns
    -------
    str
        country code as a string
    str
        area code as a string
    str
        remaining local telephone number as a string

    """
    country = s[1:3]
    area = s[3:7]
    main = s[7:13]

    return country, area, main
