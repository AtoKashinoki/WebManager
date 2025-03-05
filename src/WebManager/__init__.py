"""
    WebManager library

This file contains the WebManager-relate tools used for developing in webpages.
"""


""" Tools """


try:
    from .Webpage import WebpageManager
    ...
except ModuleNotFoundError:
    WebpageManager = ModuleNotFoundError("WebPageManager")
    ...
