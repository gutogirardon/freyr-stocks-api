"""
Freyr - A Free stock API
"""


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name
