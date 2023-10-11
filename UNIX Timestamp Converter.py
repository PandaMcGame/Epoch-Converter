import time


def epoch_to_datetime(epoch_time: int) -> str:
    """
    Convert Epoch time to a formatted datetime string.

    Args:
        epoch_time (int): The Epoch time to convert.

    Returns:
        str: A formatted datetime string (e.g., 'YYYY-MM-DD HH:MM:SS').
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch_time))


def datetime_to_epoch(datetime_str: str) -> int:
    """
    Convert a formatted datetime string to Epoch time.

    Args:
        datetime_str (str): A formatted datetime string (e.g., 'YYYY-MM-DD HH:MM:SS').

    Returns:
        int: The corresponding Epoch time.
    """
    return int(time.mktime(time.strptime(datetime_str, '%Y-%m-%d %H:%M:%S'))
