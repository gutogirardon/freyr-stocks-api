"""
Freyr - A Free stock API
"""
from bs4 import BeautifulSoup
from freyr.models.indexes import Indexes


def yahoo_finance(response):
    """
    Receive and parse data with BeautifulSoup from yahoo
    :param response:
    :return: Indexes list of obj
    """
    indexes = []
    content = BeautifulSoup(response.content, 'lxml')

    for item in content.select('[class*="data-row"]'):
        ticker = item.select('.data-col0')[0].get_text()
        name = item.select('.data-col1')[0].get_text()
        last_price = item.select('.data-col2')[0].get_text()
        change = item.select('.data-col3')[0].get_text()
        per_cent_change = item.select('.data-col4')[0].get_text()
        volume = item.select('.data-col5')[0].get_text()
        index = Indexes(ticker, name, last_price, change, per_cent_change, volume)
        indexes.append(index)

    return indexes
