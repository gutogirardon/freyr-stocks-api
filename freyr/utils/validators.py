"""
Freyr - A Free stock API
"""
from freyr.utils.exception import UnicornException


def check_params(period, interval):
    """

    :param period:
    :return:
    """
    status = False
    available_period = [
        "1d", "5d", "7d", "1mo",
    ]
    available_interval = [
        "1m", "2m", "5m", "15m", "30m", "60m", "1d", "5d", "1wk", "1mo"
    ]
    if period.lower() in available_period and interval.lower() in available_interval:
        if period.lower() == "1mo" and interval.lower() == '1m':
            raise UnicornException(name="Wrong Period or Interval!")
    else:
        raise UnicornException(name="Wrong Period or Interval!")


