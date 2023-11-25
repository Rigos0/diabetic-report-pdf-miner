import re
from typing import Union


def split_string_two_floats(s: str) -> tuple:
    """
    Splits a string into two float values.
    :param s: input string
    :return: tuple containing two float values
    """
    # Replace comma with dot for float conversion
    s = s.replace(',', '.')
    s = s.replace('mmol/l', '')

    # Split the string into two parts
    parts = s.split('±')

    # Convert each part into a float
    float_values = [float(part.strip()) for part in parts]
    str_values = [str(x) for x in float_values]

    return tuple(str_values)


def extract_float_as_str(s: str) -> Union[str, None]:
    """
    Extracts the first float value from a string.
    :param s: input string
    :return: first float value in the string
    """
    # Find the first piece of string that matches the float format
    match = re.search(r'\d+,\d+|\d+', s)

    if match:
        # Replace comma with dot for float conversion
        float_str = match.group().replace(',', '.')
        return str(float(float_str))

    return None
