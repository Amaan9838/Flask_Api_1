# flake8: noqa: F401
# noreorder
"""
pytube_age: a very serious Python library for downloading YouTube Videos.
"""
__title__ = "pytube_age"
__author__ = "AMAAN9838"
__license__ = "The Unlicense (Unlicense)"
__js__ = None
__js_url__ = None

from pytube_age.version import __version__
from pytube_age.streams import Stream
from pytube_age.captions import Caption
from pytube_age.query import CaptionQuery, StreamQuery
from pytube_age.__main__ import YouTube
from pytube_age.contrib.playlist import Playlist
from pytube_age.contrib.channel import Channel
from pytube_age.contrib.search import Search
