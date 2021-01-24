"""
Freyr - A Free stock API
"""
import requests
import requests_cache

import yfinance as yf

from freyr.services.scrape import yahoo_finance
from freyr.utils.agents import default_user_agent
from freyr.utils.exception import UnicornException
from freyr.utils.feeds import cache_time, feeds_data
from freyr.utils.logging import create_logger
from freyr.utils.validators import check_params

# Register log system
logger = create_logger("requests", "INFO")


def req_data():
    """
    Make a request to a target url
    @todo select best feeds_data and send to the correct parse (yahoo_finance)

    :return:
    """
    # Cache to new requests
    requests_cache.install_cache('indexes_finance', backend='sqlite', expire_after=cache_time)

    # @todo pick better feed server
    url = feeds_data["yahoo"]

    try:
        default_user_agent()
        response = requests.get(url, timeout=5)
        indexes = yahoo_finance(response)
    except requests.exceptions.Timeout:
        logger.error("ERROR: exceptions.Timeout")
        raise UnicornException(name="maximum time exceeded")
    except Exception as e:
        logger.error(F"ERROR: req_data: {e}")
        raise UnicornException(name="Request Error")
    return indexes


def req_yfinance_data(ticker, period="1d", interval="1d", retry=0):
    """
    Get data from yahoo api!
    :param ticker:
    :param period: 1d, 5d , 7d, 1mo
    :param interval: 1m, 2m, 5m, 15m, 30m, 60m, 1d, 5d, 1wk, 1mo
    :param retry: integer
    :return:
    """
    def yfinance_download():
        data = yf.download(tickers=ticker, period=period, interval=interval, group_by='ticker',
                           auto_adjust=True, prepost=False, threads=True, proxy=None)
        return data

    # Check period and interval
    check_params(period, interval)
    # Download data
    data = yfinance_download()
    # Parse data to dict
    data = data.to_dict()

    if len(data['Open']) == 0 and retry == 0:
        ticker = ticker+".SA"
        data = yfinance_download()
        data = data.to_dict()

    if len(data['Open']) == 0:
        logger.error(F"ERROR: req_yfinance: not found {ticker}")
        raise UnicornException(name=f"No data found, symbol may be unlisted - {ticker}")
    data['ticker'] = ticker
    data['period'] = period
    data['interval'] = interval

    return data

