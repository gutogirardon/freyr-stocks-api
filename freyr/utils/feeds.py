"""
Freyr - A Free stock API
"""
import requests
import time

# Feeds to scraping
feeds_data = {
    "yahoo": "https://in.finance.yahoo.com/world-indices",
    "investing": "https://www.investing.com/indices/major-indices",
    "trading": "https://www.tradingview.com/markets/indices/quotes-major/"
}
# default cache time (in seconds)
cache_time = 180


def feed_ping():
    """
    Check and select the better (lowest ping) data feed
    :return:
    """
    feed_dict = {}
    for i in feeds_data:
        try:
            response = requests.get(feeds_data.get(i), timeout=5)
            time_elapsed = response.elapsed.total_seconds()
            feed_dict[i] = time_elapsed
        except Exception as e:
            print(f"erro ao recuperar {i} - erro: {e}")
            pass
    lowest_feed = min(feed_dict, key=feed_dict.get)
    feed_dict.clear()
    del feed_dict
