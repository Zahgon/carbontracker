import logging
from logging import LogRecord
import os
import sys
import pathlib
import datetime
import importlib_metadata as metadata
from carbontracker import constants
from typing import Union


def convert_to_timestring(seconds: int, add_milliseconds=False) -> str:
    negative = False
    if seconds < 0:
        negative = True
        seconds = abs(seconds)

    m, s = divmod(seconds, 60)
    if not add_milliseconds:
        s = int(round(s))
        if s == 60:
            m += 1
            s = 0
    else:
        if f"{s:05.2f}"[0:2] == "60":
            m += 1
            s = 0
    h, m = divmod(m, 60)
    h = int(h)
    m = int(m)
    if not add_milliseconds:
        return f"-{h:d}:{m:02d}:{s:02d}" if negative else f"{h:d}:{m:02d}:{s:02d}"
    else:
        return f"-{h:d}:{m:02d}:{s:05.2f}" if negative else f"{h:d}:{m:02d}:{s:05.2f}"


class TrackerFormatter(logging.Formatter):
    converter = datetime.datetime.fromtimestamp

    def formatTime(self, record: LogRecord, datefmt: Union[str, None] = None) -> str:
        pass


class VerboseFilter(logging.Filter):
    def __init__(self, verbose):
        super().__init__()
        self.verbose = verbose

    def filter(self, record):
        pass


class Logger:
    def __init__(self, log_dir=None, verbose=0, log_prefix="", logger_id="root"):
        self.verbose = verbose
        self.logger, self.logger_output, self.logger_err = self._setup(
            log_dir=log_dir, log_prefix=log_prefix, logger_id=logger_id
        )
        self._log_initial_info()
        self.msg_prepend = "CarbonTracker: "

    def _setup(self, log_dir=None, log_prefix="", logger_id="root"):
        pass

    def _log_initial_info(self):
        pass

    def output(self, msg, verbose_level=0):
        pass

    def info(self, msg):
        pass

    def err_debug(self, msg):
        pass

    def err_info(self, msg):
        pass

    def err_warn(self, msg):
        pass

    def err_critical(self, msg):
        pass
