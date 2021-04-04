import logging
from logging import NullHandler
from pyradios.radios import RadioBrowser

version_info = (0, 0, 22)

__version__ = version = '.'.join(map(str, version_info))

__all__ = ["RadioBrowser"]

logging.getLogger(__name__).addHandler(NullHandler())
